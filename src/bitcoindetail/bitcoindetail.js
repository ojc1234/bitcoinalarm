import React from "react";
function bitcoindetail(props) {
  return(

  // eslint-disable-next-line no-unreachable
  <div className="detailframe">
    <div>{props.coinname} 현제정보</div>
    <div>
      <ul>
        <li>최고가:90</li>
        <li>최저가:80</li>
      </ul>
    </div>
    <div>
      <a href="https://www.naver.com">자세히 보기</a>
    </div>
{/* <iframe src="http://comci.kr:4082/st"></iframe> */}
  </div>)
}
export default bitcoindetail;