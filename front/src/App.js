
import "./App.css";
import React, { useState, useEffect } from "react";

const BASE_URL = "http://api:8000/";
// const BASE_URL = "http://api-insta.thana.team:80/";


function App() {
  const [post, setPosts] = useState([]);
  console.log(BASE_URL + "post/all/");
  useEffect(() => {
    fetch(BASE_URL + "post/all")
      .then((response) => {
        console.log(response.json());
        if (response.ok) {
          return response.json();
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
