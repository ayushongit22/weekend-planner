import streamlit as st
import requests
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))  # Add project root to path
from restaurants.restaurant import get_restaurants, process_restaurant_urls
API_URL = "https://971a380e2ad4.ngrok-free.app/ask"
CINEMAS_API_URL = "https://971a380e2ad4.ngrok-free.app/cinemas"


st.set_page_config(page_title="VentureScan AI", page_icon="🔍")
st.title("🔍 VentureScan AI")

query = st.text_input("Enter your prompt:")
# api_key = st.text_input("API Key", type="password")
submit = st.button("Submit")

def render_object(obj: dict):
    """Render any dictionary object in a card format"""
    with st.container():
        # Display primary title (first string field)
        title_key = next((k for k in obj if 'name' in k.lower() or 'title' in k.lower()), None)
        title = obj.get(title_key, "Untitled") if title_key else "Untitled"
        st.markdown(f"### {title}")

        # Image handling (if available)
        image_key = next((k for k in obj if "image" in k.lower() or "photo" in k.lower()), None)
        if image_key:
            image_val = obj.get(image_key)
            if isinstance(image_val, list) and image_val:
                st.image(image_val[0], use_container_width=True)
            elif isinstance(image_val, str):
                st.image(image_val, use_container_width=True)

        # Loop through all other fields
        for key, value in obj.items():
            if key == title_key or key == image_key:
                continue
            if isinstance(value, dict):
                st.markdown(f"**{key.title()}**:")
                for subkey, subval in value.items():
                    st.markdown(f"- {subkey.title()}: {subval}")
            elif isinstance(value, list):
                if all(isinstance(i, dict) for i in value):
                    st.markdown(f"**{key.title()}**:")
                    for idx, item in enumerate(value, 1):
                        with st.expander(f"{key.title()} {idx}"):
                            for k, v in item.items():
                                st.markdown(f"- {k.title()}: {v}")
                else:
                    st.markdown(f"**{key.title()}**: {', '.join(map(str, value))}")
            else:
                st.markdown(f"**{key.replace('_', ' ').title()}**: {value}")

        st.divider()

if submit:
    if not query or not api_key:
        st.warning("Please enter both a prompt and API key.")
    else:
        with st.spinner("Thinking..."):
            try:
                response = requests.post(API_URL, json={"query": query, "api_key": api_key})
                result = response.json()

                if response.status_code == 200:
                    event_type = result.get("event_type")
                    location = result.get("location")
                    st.success(f"**{event_type.upper()}** in **{location.title()}**")

                    if event_type == "cinemas":
                        # 👇 Call your /cinemas API automatically!
                        cinemas_res = requests.get(CINEMAS_API_URL, params={"city": location})
                        
                        if cinemas_res.status_code == 200:
                            cinema_result = cinemas_res.json()
                            data = cinema_result.get("cinemas", [])
                            st.session_state.cinema_data = data
                            st.info(f"**Found {len(data)} cinemas in {location.title()}:**")
                            if not data:
                                st.info("No results found.")
                            
                                # for item in data:
                                #     if isinstance(item, dict):
                                #         render_object(item)
                                #     else:
                                #         st.write(item)
                            # else:
                            #     st.write(data)

                        else:
                            st.error(f"Failed to fetch cinemas: {cinemas_res.text}")

                    elif event_type == "restaurants":
                        st.session_state.data = result
                        st.session_state.cuisines_list = []
                        st.session_state.address = result.get("address")
                        st.session_state.lat = result.get("latitude")
                        st.session_state.long = result.get("longitude")
                        for cuisine in result.get("data", []):
                            st.session_state.cuisines_list.append(cuisine.get("label", "Unknown"))
                        
                    else:
                        data = result.get("data", [])
                        if not data:
                            st.info("No results found.")
                        elif isinstance(data, list):
                            for item in data:
                                if isinstance(item, dict):
                                    render_object(item)
                                else:
                                    st.write(item)
                        else:
                            st.write(data)

                else:
                    st.error(f"Error {response.status_code}: {result.get('detail')}")

            except Exception as e:
                st.error(f"Failed to connect to API: {str(e)}")

if 'cuisines_list' in st.session_state:
    result = st.session_state.data
    selected = st.selectbox("Select cuisine:", ["Select..."] + st.session_state.cuisines_list)
    if selected != "Select...":
        for cuisine in result.get("data", []):
            if cuisine.get("label") == selected:
                cuisine_id = cuisine.get("id")
                break
        urls = get_restaurants(cuisine_id,st.session_state.address, st.session_state.lat, st.session_state.long)
        if urls:
            restaurant_data = process_restaurant_urls(urls)
            if restaurant_data:
                # st.success(f"**Found {len(restaurant_data)} restaurants in {location.title()}:**")
                for item in restaurant_data:
                    if isinstance(item, dict):
                        render_object(item)
                    else:
                        st.write(item)
            else:
                st.error("Failed to fetch restaurant data.")
        else:
            st.error("Failed to fetch restaurant URL.")
if 'cinema_data' in st.session_state:
    cinema_map = {c["cinema_name"].strip(): c for c in st.session_state.cinema_data}
    selected = st.selectbox("Select cinema:", ["Select..."] + list(cinema_map.keys()))

    if selected != "Select...":
        selected_cinema = cinema_map[selected]
        st.success(f"You selected: **{selected}**")
        st.markdown(f"**Cinema URL:** [{selected_cinema['url']}]({selected_cinema['url']})")
        st.markdown(f"**City:** {selected_cinema.get('city')}")
        st.markdown(f"**State:** {selected_cinema.get('state')}")
        st.write("👉 Here you can now call `/cinema_shows` to fetch shows!")
        # Trigger show fetcher
        if st.button("Get Showtimes for this Cinema"):
            with st.spinner("Fetching shows..."):
                payload = {
                    "cinema_name": selected_cinema["cinema_name"],
                    "url": selected_cinema["url"],
                    "city": selected_cinema.get("city"),
                    "state": selected_cinema.get("state"),
                    "country": selected_cinema.get("country"),
                    "date": selected_cinema.get("date"),
                }

                res = requests.post("https://971a380e2ad4.ngrok-free.app/cinema_shows", json=payload)
                shows_data = res.json()

                if res.status_code == 200:
                    shows = shows_data["shows"]
                    st.success(f"Found {len(shows)} shows:")
                    for item in shows:
                        if isinstance(item, dict):
                            render_object(item)
                        else:
                            st.write(item)
                else:
                    st.error(f"Error {res.status_code}: {shows_data.get('detail')}")