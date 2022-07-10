import logo from "./logo.svg";
import "./App.css";
import React, { Component, useEffect } from "react";
import Bitcoindetail from "./bitcoindetail/bitcoindetail";
import Sitename from "./sitename/sitename";
import { useState } from "react";
import axios from "axios";
/*

          */
//state["BTC"]["closing_price"]
function App() {
  const [state, statefun] = useState({"price" : 0});
  //statefun(axios.get("https://api.bithumb.com/public/ticker/ALL_KRW"));
  console.log(state)
  return (
    <div className="App">
      <header className="App-header">
        <Sitename className="App-name" />
        <button
          onClick={() => {
            axios
              .get("https://api.bithumb.com/public/ticker/ALL_KRW")
              .then((value) => {
                statefun({"price" : value});
              });
          }}
        >
          클릭
        </button>
        <div className="bitcoin_detail_list">
          <Bitcoindetail coinname="비코" price={state["price"]} symbol="BTC"/>
          <Bitcoindetail coinname="이더" price={state["price"]} symbol="ETH"/>
          <Bitcoindetail coinname="리플" price={state["price"]} symbol="XRP"/>
        </div>
      </header>
    </div>

  
  );
}
export default App;
