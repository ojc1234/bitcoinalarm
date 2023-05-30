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
  const [backgroundColor, backgroundColorSet] = useState({ color: "#9040FF" });

  //statefun(axios.get("https://api.bithumb.com/public/ticker/ALL_KRW"));
  console.log(state);
  const [coinlist,setcoinlist] = [useState({list : ["BTC", "ETH", "XRP"]})]
  console.log(coinlist[0])
  return (
    <div className="App">
      <div className="App-nav"><ListColor className="ListColor" /></div>
      <header className="App-header" style={{ backgroundColor: backgroundColor.color }}>
        <Sitename className="App-name" />
        <AjaxButton stateSet={stateSet} />
        <div className="bitcoin_detail_list">
          {coinlist[0].list.map( function(a,i)  {return <Bitcoindetail coinname={a} price={state["price"]} symbol={a} id = {"coin"+ i } />})}
        </div>
      </header>
    </div>
  );
}
export default App;
