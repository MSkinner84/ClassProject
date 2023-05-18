import requests


def main():
  # Prompt the user for their city or zip code
  location = input("Enter your city or zip code: ")

  # Validate the input
  if not location:
    print("Invalid input. Please try again.")
    return

  # Get the weather data
  weather_data = get_weather_data(location)

  # Display the weather data to the user
  if weather_data:
    display_weather_data(weather_data)
  else:
    print("Failed to retrieve weather data. Please try again.")


def get_weather_data(location):
  try:
    # Send a GET request to openweathermap.org with the user's location
    response = requests.get(
      f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid=46ecb770f8d839302f0082fc0a2f5e4d"
    )

    # Check if the response was successful
    if response.status_code == 200:
      # Convert the response data to JSON format
      data = response.json()
      return data
    else:
      print("Failed to retrieve weather data. Response code:",
            response.status_code)
      return None
  except:
    print("Failed to establish connection with openweathermap.org API.")
    return None


def display_weather_data(data):
  # Extract the relevant weather information from the JSON object
  city = data["name"]
  temperature = round(data["main"]["temp"] - 273.15, 2)
  humidity = data["main"]["humidity"]
  description = data["weather"][0]["description"]

  # Display the weather information to the user
  print(f"City: {city}")
  print(f"Temperature: {temperature}°C")
  print(f"Humidity: {humidity}%")
  print(f"Description: {description}")


# Allow the user to run the program multiple times
while True:
  main()
  # Ask the user if they want to check the weather again
  answer = input("Do you want to check the weather again? (y/n): ")
  if answer.lower() != "y":
    break
