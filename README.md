# mern-template

A template for MERN stack applications
-
* Includes Express.js backend with database integration using MongoDB and Mongoose, which has a basic User model with fields name, email and password.
* Includes jwt authentication
* Includes Vite+React frontend, implemented with Redux Toolkit.
* For CSS, TailwindCSS and DaisyUI have been used, along with React Toastify.
* Also includes a theme switcher for light and dark mode preferences! 

Will keep updating this template with improvements.

Thanks for reading!

Instructions 
-
To run this app, just execute `npm install` in the root directory and also the frontend folder. After that set up a .env file in the root directory with the following fields:
* NODE_ENV=development
* PORT=5000
* MONGO_URI=YOUR_MONGODB_CONN_STRING
* JWT_SECRET=ANY_VALUE_YOU_WANT


After this, just execute `npm run dev` in the root directory and both the frontend(port=3000) and backend(port=5000) server will start.
