## APIs are everywhere

1. What is API?
API is the acronym for **Application Programming Interface**, which is a mechanism that enables two softwares/applications to communicate with each other based on a set of standards and protocols. 

Mostly known und mostly used APIs are web APIs. A lot of companies have accumulated or generated a lot of data and produce APIs to either share these data to their partner or to sell these data per API call. For example, the weather bureau’s system contains daily weather data and we want to develop an app to display this weather information daily on the phone, our app needs to connect to bureau's system via APIs to retrieve the data. In this context, our app acts as a client application, which sends a request to the web server of the bureau and receives a response with the requested information, typically in JSON format. API calls usually requires authentification and authorisation to prevent the risk of attack on the server.

2. Why are APIs becoming more popular?
APIs are increasingly important and popular over the past decade. It is not overreacting at all to say that many web applications would not be made possible without APIs. How so? Firstly, APIs improve collaboration between companies, business partners and even amongst developers, by making data exchange so much easier. Without APIs, software developers would have a much harder time writing code to get information from platforms or apps they want to access. Secondly, because of monetisation many companies who own a good database are selling "data as a service" and APIs just make it easier to implement. 

3. How to use APIs
Typically nowadays when you want to use APIs from a provider, you need to obtain an API Key, which is easily done by going to their website and register an account. After that you can use multiple programming languages (Java, Javascript, Python, Perl and Ruby) to retrieve the data with the API key you received. Usually the provider will provide a defined syntax on their API documentation, so that you can easily apply them on your application. API requests have several methods, such as POST (send data/input), GET (retrieve data), PUT (update data) and DELETE (delete data). 

As a practical example I will demonstrate how I use API to retrieve and weather information and display it on my small website I built as part of my learning process. The demo link can be found [here](https://musing-darwin-6b02d3.netlify.app/). If you are interested in how to publish an app with Netlify, kindly let me know in the comment.

You will need to go to [Open Weather Map](https://openweathermap.org/) to create an account and get your API key. After that you can try to see if it works on your browser by enter this in any browser. Remember to substitute 3 variables, such as {lat}, {lon} and of course your {API key}.

```
https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}

or

https://api.openweathermap.org/data/2.5/weather?lat=-122&lon=37&appid={API key}

or

https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}

or

https://api.openweathermap.org/data/2.5/weather?q=London&appid={API key}
``` 

Then you will see the result directly in your browser in form of a JSON.


```
{
  "coord": {
    "lon": -122.08,
    "lat": 37.39
  },
  "weather": [
    {
      "id": 800,
      "main": "Clear",
      "description": "clear sky",
      "icon": "01d"
    }
  ],
  "base": "stations",
  "main": {
    "temp": 282.55,
    "feels_like": 281.86,
    "temp_min": 280.37,
    "temp_max": 284.26,
    "pressure": 1023,
    "humidity": 100
  },
  "visibility": 10000,
  "wind": {
    "speed": 1.5,
    "deg": 350
  },
  "clouds": {
    "all": 1
  },
  "dt": 1560350645,
  "sys": {
    "type": 1,
    "id": 5122,
    "message": 0.0139,
    "country": "US",
    "sunrise": 1560343627,
    "sunset": 1560396563
  },
  "timezone": -25200,
  "id": 420006353,
  "name": "Mountain View",
  "cod": 200
  }        
``` 

You can now access the elements of your interest from the JSON from your code, either in Python or in Javascript or other languagues. 


```
function getWeatherData(searchedCity) {
    fetch(api.url + "q=" + searchedCity + "&units=metric&APPID=" + api.key)
        .then((response) => response.json())
        .then((data) => {
            $(".city").html(data["name"] + ", " + data["sys"]["country"]);
            $(".temp").html(data["main"]["temp"] + "&#8451;");
            $(".description").html(data["weather"][0]["description"]);
            $(".minmax").html(
                "min: " + data["main"]["temp_min"] +
                "&#8451; | " +
                "max: " + data["main"]["temp_max"] +
                "&#8451;"
            );
        })
        .catch((error) => console.log(error));
}
``` 
Here is an example of creating a function in JS to send the request with "searchedCity" as input from user and the api key. Because I want the result in metric format, which means in celsius and not fahrenheit, I add in my request "units=metric". Once I have the response, I convert it into JSON and access the city name, the temp (within "main" block), description and min/max temperature. 

Thanks for reading and I hope it is helpful in some ways :)

