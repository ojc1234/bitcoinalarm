import logo from "./logo.svg";
import "./App.css";
import React, { Component, useEffect } from "react";
import Sitename from "./component/sitename/sitename";
import { useState } from "react";
import axios from "axios";
import AjaxButton from "./component/ajax_botton/button"
import ListColor from "./component/color_changings/color_changings"
import Bitcoindetail from "./component/bitcoindetail/bitcoindetail";
//state["BTC"]["closing_price"]
function App() {
  const [state, stateSet] = useState({ price: 0 });
  const [backgroundColor, backgroundColorSet] = useState({ color: "#9040FF"});

  //statefun(axios.get("https://api.bithumb.com/public/ticker/ALL_KRW"));
  console.log(state);
  return (
    <div className="App">
      <div className="App-nav"><ListColor className="ListColor"/></div>
      <header className="App-header" style={{backgroundColor:backgroundColor.color}}>
        <Sitename className="App-name" />
        <AjaxButton stateSet = {stateSet}/>
        <div className="bitcoin_detail_list">
          <Bitcoindetail coinname="비코" price={state["price"]} symbol="BTC" />
          <Bitcoindetail coinname="이더" price={state["price"]} symbol="ETH" />
          <Bitcoindetail coinname="리플" price={state["price"]} symbol="XRP" />
        </div>
      </header>
    </div>
  );
}
export default App;
