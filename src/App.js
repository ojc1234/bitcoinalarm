import logo from "./logo.svg";
import "./App.css";
import React from "react";
import Bitcoindetail from "./bitcoindetail/bitcoindetail";
import { render } from "react-dom";
import Sitename from "./sitename/sitename";

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <Sitename className="App-name"/>
        <div className="bitcoin_detail_list">
          <Bitcoindetail coinname="비코" />
          <Bitcoindetail coinname="이더" />
          <Bitcoindetail coinname="도지" />
        </div>
      </header>
    </div>
  );
}

export default App;
