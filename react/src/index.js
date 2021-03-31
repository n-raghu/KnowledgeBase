import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap";
import React from "react";
import { render } from "react-dom";
import App from "./components/App";
import { MemoryRouter as Router } from "react-router-dom";

render(
  <Router>
    <App />
  </Router>,
  document.getElementById("root")
);
