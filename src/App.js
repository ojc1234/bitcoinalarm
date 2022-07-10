import logo from "./logo.svg";
import "./App.css";
import React, { Component, useEffect } from "react";
import Bitcoindetail from "./bitcoindetail/bitcoindetail";
import { render } from "react-dom";
import Sitename from "./sitename/sitename";
import { useState } from "react";
import axios from "axios";
/*

          */
//state["BTC"]["closing_price"]
function App() {
  const [state, statefun] = useState(0);
  //statefun(axios.get("https://api.bithumb.com/public/ticker/ALL_KRW"));
  useEffect(() => {
    if (typeof state == "object") {
      // 브라우저 API를 이용하여 문서 타이틀을 업데이트합니다.
      document.title = state.data["data"]["BTC"]["closing_price"];
      document.querySelector(".detailframe > div:nth-child(4n)").innerHTML = `${state.data["data"]["BTC"]["closing_price"]}`;
    } else document.title = `You clicked ${0} times`;
  });
  return (
    <div className="App">
      <header className="App-header">
        <Sitename className="App-name" />
        <button
          onClick={() => {
            axios
              .get("https://api.bithumb.com/public/ticker/ALL_KRW")
              .then((value) => {
                statefun(value);
              });
          }}
        >
          클릭
        </button>
        <div className="bitcoin_detail_list">
          <Bitcoindetail coinname="비코" price={0} className="bitcoinprice" />
          <Bitcoindetail coinname="이더" price={0} />
          <Bitcoindetail coinname="도지" price={0} />
        </div>
      </header>
    </div>
  );
}

export default App;
