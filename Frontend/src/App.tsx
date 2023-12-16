import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import {Button} from "react-bootstrap";

import Flickity from "react-flickity-component";
import Carousel from "./components/utils/carousel/Carousel";
import Menu from "./components/utils/menu/Menu";
import {NewsPage} from "./components/pages/NewsPage/NewsPage";
import {EventsPage} from "./components/pages/EventsPage/EventsPage";

function App() {
  const flickityOptions = {
    initialIndex: 2
  }

  return (
    <div>

      <EventsPage />
    </div>
  );
}

export default App;
