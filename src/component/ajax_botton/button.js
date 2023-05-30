import React from "react"
import axios from "axios";
export default function hello(props) {
  return (

    <button
      onClick={() => {
        setInterval(() => {
          axios
            .get("https://api.bithumb.com/public/ticker/ALL_KRW")
          .then((value) => {
            props.stateSet({ price: value });
          })
          .catch(() => {
            props.stateSet({ price: 0 });
          });
        }, 100)

      }}
    >
      클릭
    </button>
  )
}