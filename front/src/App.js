
import "./App.css";
import React, { useState, useEffect } from "react";

const BASE_URL = "https://api-insta.thana.team/";


function App() {
  const [post, setPosts] = useState([]);
  useEffect(() => {
    fetch(BASE_URL + "post/all")
      .then((response) => {

        if (response.clone().ok) {
          return response.clone().json();
        }
        throw response;
      })
      .then((data) => {
       setPosts(data);
      })
      .catch((error) => {
     console.log(error);
      alert(error);
      });
  }, []);
  return "Hello world";
}

export default App;
