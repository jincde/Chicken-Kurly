import React from 'react';

const Footer = () => {
    return (
        <div>
            <div id="footer">
                <div className="footer__info">
                    <div className="inquiry">
                        <h2>고객행복센터
                            <span>365일 오전 7시 - 오후 7시</span>
                        </h2>
                        <strong>1644-1107</strong>
                        <div className="inquiry-sns">
                            <button className="inquiry-item">카카오톡 문의</button>
                            <button className="inquiry-item">1:1 문의</button>
                            <button className="inquiry-item">대량주문 문의</button>
                        </div>
                        <div className="inquiry-mail">
                            비회원 문의 : <a href="mailto:help@kurlycorp.com">kurlygift@kurlycorp.com</a>
                            <br/>
                            비회원 대량주문 문의 : <a href="mailto:kurlygift@kurlycorp.com">kurlygift@kurlycorp.com</a>
                        </div>
                    </div>

                                
                    <div className="company-info">
                        <ul className="company__intro">
                            <li><a href="https://www.kurly.com/shop/introduce/about_kurly.php" target="_self">컬리소개</a></li>
                            <li><a href="https://www.kurly.com/shop/introduce/about_kurly.php" target="_self">컬리소개영상</a></li>
                            <li><a href="https://www.kurly.com/shop/introduce/about_kurly.php" target="_self">인재채용</a></li>
                            <li><a href="https://www.kurly.com/shop/introduce/about_kurly.php" target="_self">이용약관</a></li>
                            <li><a href="https://www.kurly.com/shop/introduce/about_kurly.php" target="_self">개인정보처리방침</a></li>
                            <li><a href="https://www.kurly.com/shop/introduce/about_kurly.php" target="_self">이용안내</a></li>
                        </ul>
                        <div className="company__raw">
                            법인명 (상호) : 주식회사 컬리
                            {/* <!-- <div className="line"></div> --> */}
                            <span className="bar"></span>
                            사업자등록번호 : 261-81-23567
                            <a href="https://www.ftc.go.kr/bizCommPop.do?wrkr_no=2618123567&apv_perm_no=" target="_blank" rel="noreferrer">사업자정보 확인</a>
                            <br/>
                            통신판매업 : 제 2018-서울강남-01646 호 
                            <span className="bar"></span>
                            개인정보보호책임자 : 이원준
                            <br/>
                            주소 : 서울특별시 강남구 테헤란로 133, 18층(역삼동) 
                            <span className="bar"></span>
                            대표이사 : 김슬아
                            <br/>
                            입점문의 : 
                            <a href="https://docs.google.com/forms/d/e/1FAIpQLScLB7YkGJwNRzpGpp0gbR1i4C1_uvTEFj43SFfJ_XEadTn3gQ/viewform?usp=sf_link" target="_blank" rel="noreferrer">입점문의하기</a>
                            <span className="bar"></span>
                            제휴문의 :
                            <a href="mailto:business@kurlycorp.com">business@kurlycorp.com</a>
                            <br/>
                            채용문의 : 
                            <a href="mailto:recruit@kurlycorp.com">recruit@kurlycorp.com</a>
                            <br/>
                            팩스: 070 - 7500 - 6098
                        </div>
                        <ul className="company__sns">
                            <li><a href="https://instagram.com/marketkurly" target="_blank" rel="noreferrer"><img src="https://res.kurly.com/pc/ico/1810/ico_instagram.png" alt="마켓컬리 인스타그램 바로가기"/></a></li>
                            <li><a href="https://instagram.com/marketkurly" target="_blank" rel="noreferrer"><img src="https://res.kurly.com/pc/ico/1810/ico_fb.png" alt="마켓컬리 페이스북 바로가기"/></a></li>
                            <li><a href="https://instagram.com/marketkurly" target="_blank" rel="noreferrer"><img src="https://res.kurly.com/pc/ico/1810/ico_blog.png" alt="마켓컬리 네이버블로그 바로가기"/></a></li>
                            <li><a href="https://instagram.com/marketkurly" target="_blank" rel="noreferrer"><img src="https://res.kurly.com/pc/ico/1810/ico_naverpost.png" alt="마켓컬리 네이버포스터 바로가기"/></a></li>
                            <li><a href="https://instagram.com/marketkurly" target="_blank" rel="noreferrer"><img src="https://res.kurly.com/pc/ico/1810/ico_youtube.png" alt="마켓컬리 유튜브 바로가기"/></a></li>
                        </ul>
                       
                    </div>
                </div>

                <div className="footer__connection">
                    <button><img src="https://res.kurly.com/pc/ico/2208/logo_isms.svg" alt="isms 로고"/>
                        <p>
                            [인증범위] 마켓컬리 쇼핑몰 서비스 개발·운영
                            <br/>
                            (심사받지 않은 물리적 인프라 제외)
                            <br/>
                            [유효기간] 2022.01.19 ~ 2025.01.18
                            <br/>
                        </p>
                    </button>
                    <button><img src="https://res.kurly.com/pc/ico/2208/logo_privacy.svg" alt="isms 로고"/>
                        <p>
                            개인정보보호 우수 웹사이트 ·
                            <br/>
                            개인정보처리시스템 인증 (ePRIVACY PLUS)
                            <br/>
                        </p>
                    </button>
                    <button><img src="https://res.kurly.com/pc/ico/2208/logo_tosspayments.svg" alt="isms 로고"/>
                        <p>
                            토스페이먼츠 구매안전(에스크로)
                            <br/>
                            서비스를 이용하실 수 있습니다.
                            <br/>
                        </p>
                    </button>
                    <button><img src="https://res.kurly.com/pc/ico/2208/logo_wooriBank.svg" alt="isms 로고"/>
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

            <div className="footer-end">
                마켓컬리에서 판매되는 상품 중에는 마켓컬리에 입점한 개별 판매자가 판매하는 마켓플레이스(오픈마켓) 상품이 포함되어 있습니다.
                <br/>
                마켓플레이스(오픈마켓) 상품의 경우 컬리는 통신판매중개자로서 통신판매의 당사자가 아닙니다. 컬리는 해당 상품의 주문, 품질, 교환/환불 등 의무와 책임을 부담하지 않습니다.
                <br/>
                <em>© KURLY CORP. ALL RIGHTS RESERVED</em>
            </div>

        </div>
    );
};

export default Footer;