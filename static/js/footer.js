import "./Footer.css";

function Footer() {
  return (<div class="benner">
    <div class="footer">
      <div class="up_footer">
        <div class="up_up_footer">
          <div class="left_div">
            <h2>
              고객행복센터
              <span>365일 오전 7시 - 오후 7시</span>
            </h2>
            <strong>1644-1107</strong>
            <div class="footer_btn">
              <button>카카오톡 문의</button>
              <button class="footer_btn2">1:1 문의</button>
              <button class="footer_btn2">대량주문 문의</button>
            </div>
            <div class="footer_email">
              비회원 문의:
              <a href="mailto:help@kurlycorp.com">help@kurlycorp.com</a>
              <br/>
              비회원 대량주문 문의 :
              <a href="mailto:kurlygift@kurlycorp.com">
                kurlygift@kurlycorp.com
              </a>
            </div>
          </div>
          <div class="right_div">
            <ul class="right_div_ul">
              <li class="right_li">
                <a href="https://www.kurly.com/shop/introduce/about_kurly.php" target="_self" class="right_a">
                  컬리소개
                </a>
              </li>
              <li class="right_li2">
                <a href="https://www.youtube.com/embed/WEep7BcboMQ?rel=0&amp;showinfo=0&amp;wmode=opaque&amp;enablejsapi=1" target="_self" class="right_a">
                  컬리소개영상
                </a>
              </li>
              <li class="right_li2">
                <a href="https://marketkurly.recruiter.co.kr/appsite/company/index" target="_blank" class="right_a">
                  인재채용
                </a>
              </li>
              <li class="right_li2">
                <a href="/user-terms/agreement" target="_self" class="right_a">
                  이용약관
                </a>
              </li>
              <li class="right_li2">
                <a href="/user-terms/privacy-policy" target="_self" class="right_a">
                  개인정보처리방침
                </a>
              </li>
              <li class="right_li2">
                <a href="/user-guide" target="_self" class="right_a">
                  이용안내
                </a>
              </li>
            </ul>
            <div class="right_info">
              법인명 (상호) : 주식회사 컬리
              <span class="right_info_span"></span>
              사업자등록번호 : 261-81-23567
              <a href="https://www.ftc.go.kr/bizCommPop.do?wrkr_no=2618123567&amp;apv_perm_no=" target="_blank" rel="noreferrer" class="css-1tby8gd ebj6vxr0">
                사업자정보 확인
              </a>
              <br/>
              통신판매업 : 제 2018-서울강남-01646 호
              <span class="right_info_span"></span>
              개인정보보호책임자 : 이원준
              <br/>
              주소 : 서울특별시 강남구 테헤란로 133, 18층(역삼동)
              <span class="right_info_span"></span>
              대표이사 : 김슬아
              <br/>
              입점문의 :
              <a href="https://docs.google.com/forms/d/e/1FAIpQLScLB7YkGJwNRzpGpp0gbR1i4C1_uvTEFj43SFfJ_XEadTn3gQ/viewform?usp=sf_link" target="_blank" rel="noreferrer" class="css-1tby8gd ebj6vxr0">
                입점문의하기
              </a>
              <span class="right_info_span"></span>
              제휴문의 :
              <a href="mailto:business@kurlycorp.com" class="css-1tby8gd ebj6vxr0">
                business@kurlycorp.com
              </a>
              <br/>
              채용문의 :
              <a href="mailto:recruit@kurlycorp.com" class="css-1tby8gd ebj6vxr0">
                recruit@kurlycorp.com
              </a>
              <br/>
              팩스: 070 - 7500 - 6098
            </div>
          </div>
        </div>
        <div class="up_down_footer">
          <button>
            <img src="https://res.kurly.com/pc/ico/2208/logo_isms.svg" alt="isms 로고" class="up_down_footer_img"/>
            <p>
              [인증범위] 마켓컬리 쇼핑몰 서비스 개발·운영
              <br/>
              (심사받지 않은 물리적 인프라 제외)
              <br/>
              [유효기간] 2022.01.19 ~ 2025.01.18
            </p>
          </button>
          <button>
            <img src="https://res.kurly.com/pc/ico/2208/logo_privacy.svg" alt="eprivacy plus 로고" class="up_down_footer_img"/>
            <p>
              개인정보보호 우수 웹사이트 ·
              <br/>
              개인정보처리시스템 인증 (ePRIVACY PLUS)
            </p>
          </button>
          <button>
            <img src="https://res.kurly.com/pc/ico/2208/logo_tosspayments.svg" alt="payments 로고" class="toss_img"/>
            <p>
              토스페이먼츠 구매안전(에스크로)
              <br/>
              서비스를 이용하실 수 있습니다.
            </p>
          </button>
          <button>
            <img src="https://res.kurly.com/pc/ico/2208/logo_wooriBank.svg" alt="우리은행 로고" class="up_down_footer_img"/>
            <p>
              고객님이 현금으로 결제한 금액에 대해 우리은행과
              <br/>
              채무지급보증 계약을 체결하여 안전거래를 보장하고
              <br/>
              있습니다.
            </p>
          </button>
        </div>
      </div>
      <div class="down_footer">
        <em class="right">© KURLY CORP. ALL RIGHTS RESERVED</em>
      </div>
    </div>
  </div>);
}
export default Footer;
