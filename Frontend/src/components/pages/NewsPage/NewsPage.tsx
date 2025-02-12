import React from 'react';
import "./newspage.scss"
import Circle from "../../utils/circle/Circle"
import NewsCard from "../../utils/news-card/NewsCard";
import AliceCarousel from 'react-alice-carousel';
import 'react-alice-carousel/lib/alice-carousel.css';

const responsive = {
    0: { items: 1 },
    1100: { items: 2 },
    1650: { items: 3 },
    2350: { items: 4 }
};

const items = [
    <NewsCard img="news1.png" txt="День программиста" />,
    <NewsCard img="news2.png" txt="Транспорт будущего" />,
    <NewsCard img="news3.png" txt="Регистрация на Инженерный вызов 2023"/>
];

const Carousel = () => (
    <AliceCarousel
        mouseTracking
        items={items}
        responsive={responsive}
        controlsStrategy="alternate"
        disableButtonsControls={true}
        infinite={true}
    />
);

export const NewsPage = () => {
    return (
        <section className={"news-page"}>
            <Circle title="новости"/>
            <div className="news-carousel">
                <div className="desktop-carousel">
                    <Carousel/>
                </div>
                <div className="mobile-carousel">
                    {items}
                </div>
            </div>
        </section>
    )
}