import React from "react";
function bitcoindetail(props) {
  console.log(props.price.data)
  return (
    // eslint-disable-next-line no-unreachable
    <div className="detailframe">
      <div>{props.coinname} 현제정보</div>
      <div>
        <ul>
          <li>최고가:{props.price ? props.price.data["data"][props.symbol]["max_price"]:0}원</li>
          <li>최저가:{props.price ? props.price.data["data"][props.symbol]["min_price"]:0}원</li>
        </ul>
      </div>
      <div>
        <a href="https://www.naver.com">자세히 보기</a>
      </div>
      <div>
        {props.price ? props.price.data["data"][props.symbol]["closing_price"]:0}원
        {/*props.price[1]["BTC"]["closing_price"]*/}
      </div>

      {/* <iframe src="http://comci.kr:4082/st"></iframe> */}
    </div>
  );
}
export default bitcoindetail;
