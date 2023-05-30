import React, { useState } from "react";
import axios from "axios";
export default function Hello(props) {
  const css_setting = {
    "padding-botton": "0vh",
    height: "30px",
    display: "flex",
    "flex-direction": "row;",
    "text-align": "left",
    justifyContent: "left",
    width: "100vw",
  };
  const [text, setText] = useState("");
  const [btcapi, setbtcapi] = useState("");
  const onChange = (e) => {
    setText(e.target.value.toUpperCase());
  };
  return (
    <div className="App-nav" style={css_setting}>
      <div
        className="App-nav"
        style={{
          "text-align": "left",
          display: "flex",
          "flex-direction": "row;",
        }}
      >
        {props.state.list.map((a) => {
          return <div style={{ "padding-right": "30px" }}> {a} </div>;
        })}
      </div>
      <div>
        <input id="btcinput" type="" onChange={onChange} value={text}></input>
        <input
          type="submit"
          onClick={() => {
            const a = null;
            axios
              .get("https://api.bithumb.com/public/ticker/ALL_KRW")
              .then((value) => {
                setbtcapi(value);
              })
              .catch(() => {
                setbtcapi(null);
              });
            console.log(btcapi);
            var newbtclist = [...props.state.list];
            newbtclist?.push(text);
            console.log(btcapi["data"][text]);
            btcapi.data["data"][text] && props.stateSet({ list: newbtclist });
          }}
          value={"클릭시 새로운 비트코인 추가"}
        ></input>
      </div>
    </div>
  );
}
