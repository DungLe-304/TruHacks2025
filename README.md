Here is Main server created using Spring Boot: https://github.com/SteveRogersBD/TruServer2025.git

# **Green Pulse: Smart Farming for a Sustainable Future**   

## **🌍Inspiration🌱**  

40% of farmers struggle because they lack access to important farming knowledge, leading to lower yields. We want to build a community where farmers share knowledge and use AI tools to grow more food and prevent the 20 to 40% lost each year to pests and diseases. Every year, 120 billion pounds of food go to waste. By connecting farmers with local buyers, we can make fresh food more affordable and reduce waste. We also aim to improve fertilizer use to cut down the 53.65 million tones wasted yearly. Our goal is a smarter, more sustainable farming future.

## **What it does**
1. **👩‍🌾🌱 Find & save your farm info**: Keep track of your farm’s details and monitor progress in one place using google maps.  

2. **🤖🦠 Crop disease detection & solution**: Identify crop diseases early and get AI-driven solutions to protect your yield.  

3. **🌦️⚠️ Weather forecast for crop harm prediction**: Get weather-based predictions to prevent damage from extreme conditions with AI driven solutions.  

4. **🤖🌱 Ask & learn farming with chatbot**: Ask any question related to farming, then Agri-bot advices you.

5. **🌍📰 Stay tuned on global news**: Stay updated on the latest agricultural trends, policies, and market changes.  

6. **👩‍🌾🌱 Share your stories on community**: Connect with other farmers, exchange experiences, and learn from each other.  

7. **🚜📦 Sell or buy via online marketplace**: Trade fresh produce and farm supplies quickly and easily with local buyers.  

---

## **How we built it**

We built GreenPulse by integrating multiple AI models and utilizing the following tools and frameworks:

- **Google map API**: used for the functions to find farm fields and mark the area on the map
- **Google Gemini API**: we used Gemini for users to talk with chatbot and ask farming knowledge questions.
- **OpenWeatherMap API**: used to get real-time weather forecasts data and made AI model to predict climate-related crop harms.
- **Google Colab**: no GPU, so we used Google Colab and trained multiple models simultaneously by opening several Colab notebook tabs. We selected the best model. We also used early stopping method to minimize the number of epochs.
- **Torch**: used to train models for crop disease detection.
- **TorchVision**: used to preprocess, augment, and normalize tomato images.
- **Flask**:  used to run backend server. Mobile app can use AI models through it.
- **Firebase**: used for secure, scalable, and real-time data storage (farms information, user information, images, etc.)
- **Android Studio**: used to build android app
-**Spring Boot**: Used for creating the server which is connected with a MySQL database. 
- **VS code**: for writing codes for server, testing APIs, etc.
- **Plant Village Dataset**: due to lack of GPU and time, we selected only tomato images and trained model.

## **Challenges we ran into**

- **API Integration**: Balancing API rate limits and optimizing performance required meticulous planning.
- **Processing large data without GPU**: Training models on a laptop took hours, making it hard to find the best algorithm, so we had to constantly brainstorm to reduce trials, yet make speedy & accurate AI models.
- **Sustainable business**: for sustainable business & environment together, we tried to do creative thinking.
- **User Experience Design**: Many farmers are unfamiliar with digital tools, so we created an intuitive UX/UI and offer onboarding support.

## **Accomplishments & What we learned**

- **App development**: Creating an Android app with various features, such as farmer data, land location records, marketplace functionality, server communication for AI models, and the Gemini chatbot, was not easy. Testing these features also took a significant amount of time. We held numerous meetings to discuss how to make the app more intuitive and seamless for users.
- **Creative thinking**: We were able to deeply consider the feasibility of a sustainable business and reflect on the parts that need improvement for this service to be successfully launched.
- **Seamless collaboration**: We worked hard to ensure smooth collaboration between the backend and frontend teams, all while sharing the same vision to create a unified product.

---

## **What's next for GreenPulse**

- **🚚 1-day fresh delivery**: We’re developing a 1-day delivery service to ensure fresh food reaches consumers quickly.
- **🛰️Advanced Satellite analytics**: We aim to expand our satellite analysis capabilities, providing deeper insights into crop health and field conditions for better farm management.
- **🤖 Better AI model**: AI model to support wider range of crops and diseases, providing more accurate and comprehensive predictions for better farm management.
