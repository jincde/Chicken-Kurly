## :chicken::purple_heart: 치킨컬리(Chicken-Kurly) 프로젝트

**닭가슴살 러버들을 위한 건강한 식습관 공유 커뮤니티**
<br>- 겉은 바삭하고 속은 촉촉하며 나트륨이 높지 않으면서도 맛있는 닭가슴살 제품을 판매하는 쇼핑몰 사이트 Chicken Kurly
[@chickenkurly_regram](https://www.instagram.com/chickenkurly_regram/)

![carousel2](README.assets/carousel2.jpg)

---
## 목차
* [치킨컬리Chicken-Kurly) 프로젝트](#chicken-purple_heart-치킨컬리chicken-kurly-프로젝트)
  * [Contributors](#-contributors)
  * [목적](#trophy-목적)
  * [기간](#date-기간)
  * [기술 스택](#hammer_and_wrench-기술-스택)
* [팀원 소개 및 담당 역할](#technologist-팀원-소개-및-담당-역할)
* [서비스 주제](#bulb-서비스-주제)
* [주요 기능 소개](#shopping_cart-주요-기능-소개)
* [Chicken Kurly](#dart-chicken-kurly)
* [서비스 시연](#computer-서비스-시연)
* [프로젝트 후 느낀점](#purple_heart-프로젝트-후-느낀점)


---

#### ✨ Contributors

<a href="https://github.com/jincde/chicken-kurly/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=jincde/chicken-kurly" />
</a>

* [장영진](https://github.com/jincde), 
[차화영](https://github.com/forwardyoung), 
[이동현](https://github.com/soohofather), 
[최정아](https://github.com/astroastrum),
[최보영](https://github.com/jupiter6676)


### :trophy: 목적
* Django와 HTML/CSS/JavaScript 활용하여 상품 정보 및 후기 공유 커뮤니티 웹 플랫폼 서비스 개발


### :date: 기간
* 2022.11.09 ~ 2022.11.22
* 프로젝트 기획: 2022.11.09
  - [기획서](https://www.notion.so/hg-edu/bb8affdc8a644d66a34ea3d1fcb84501)
* 배포: 2022년 11월 21일



### :hammer_and_wrench: 기술 스택
<div align="left">
  <img src="https://img.shields.io/badge/Django-green?style=flat&logo=Django&logoColor=092E20"/>
  <img src="https://img.shields.io/badge/Python-blue?style=flat&logo=Django&logoColor=3776AB"/>
  <img src="https://img.shields.io/badge/CSS-pink?style=flat&logo=Django&logoColor=1572B6"/>
  <img src="https://img.shields.io/badge/JavaScript-yellow?style=flat&logo=Django&logoColor=F7DF1E"/>
  <img src="https://img.shields.io/badge/HTML-orange?style=flat&logo=Django&logoColor=E34F26"/>
  <img src="https://img.shields.io/badge/VSCODE-Full%20Stack-purple"/>
  <img src="https://img.shields.io/badge/GITHUB-black?style=flat&logo=Django&logoColor=181717"/>
</div>

---

## :technologist: 팀원 소개 및 담당 역할

<details>
<summary>장영진</summary>
<div markdown="1">
<h5>팀장</h5>
<h5>풀스택 개발</h5>
    <ul>
    <li><p>products, accounts, articles 디자인 및 백엔드 개발</p></li>
    <li><p>베이스 구현</p></li>
    </ul>
</div>
</details>
<details>
<summary>이동현</summary>
<div markdown="1">
<h5>백엔드 개발</h5>
    <ul>
    <li><h5>자유게시판 [Articles] 개발</h5></li>
    </ul>
</div>
</details>
<details>
<summary>최보영</summary>
<div markdown="1">
<h5>풀스택 개발</h5>
    <ul>
    <li><h5>상품페이지 [Products] 개발</h5></li>
    </ul>
</div>
</details>
<details>
<summary>차화영</summary>
<div markdown="1">
<h5>풀스택 개발</h5>
    <ul>
    <li><h5>상품페이지 [Products] 개발</h5></li>
    </ul>
</div>
</details>
<details>
<summary>최정아</summary>
<div markdown="1">
<h5>풀스택 개발</h5>
    <ul>
    <li><h5>회원관리 [Accounts] 개발</h5></li>
    </ul>
</div>
</details>

---

## :bulb: 서비스 주제
* 닭가슴살 식품 정보 및 후기 공유 커뮤니티 서비스
    - 신선하고 맛있는 닭가슴살 제품을 판매하는 쇼핑몰 사이트 Chicken Kurly는 상품을 한눈에 볼 수 있는 Products App, 고객님의 피드백을 반영 및 공유할 수 있는 Articles App, 회원가입과 로그인 기능을 제공하는 Accounts App으로 구성되어 있습니다. 웹 프레임워크 Django를 기반하여 사용자가 쉽게 이용할 수 있도록 사이트를 구현했습니다.



---
## :dart: Chicken Kurly
![]()
[]()![products](https://user-images.githubusercontent.com/108647883/202868016-5284776c-082e-49d0-93d3-e5e2228bc15b.gif)



---

## :shopping_cart: 주요 기능 소개

* 프론트엔드
  * 상품페이지 [Products]
    * 내비게이션 바
    * 검색 기능
    * 로고
    * 장바구니
    * 좋아요

* 상품페이지 [Products]
  * 상품 목록
    * 판매 상품 
    * 인기 상품
  * 상품 정보
    * 사용자의 후기 및 문의
      * 문의 
          * 모든 유저가 문의글을 작성할 수 있지만, 댓글은 관리자 계정만 작성가능
          * 문의에 답변이 달리면 수정 및 삭제 불가
          * 문의 페이지네이션
    * 수량/옵션 선택
    * 장바구니
      * 상품 수량 추가
        * 이전에 장바구니에 담았던 상품의 경우, 상품 수량을 추가하는 방식
    * 찜하기
        * accounts/profile.html에서 렌더 가능
    * 결제
        * 상품 결제 화면으로 이동


* 자유게시판 [Articles]
  * 게시글 CRUD
    * 자유게시판 작성
    * 자유게시판 글 보여주기
    * 자유게시판 글 수정
    * 자유게시판 글 삭제
  * 자유게시판 Comment CRUD
  * 좋아요/댓글
  * 팔로우/언팔로우


* 회원관리 [Accounts]
  * 회원가입
    * 아이디 중복확인
  * 로그인
    * 아이디/비번 오류 
  * 회원 프로필
    * 사용자 본인 - 정보 수정 버튼 렌더
    * 사용자 본인이 아닐 경우, 팔로우 버튼 렌더
    * 구매한 상품 목록
    * 찜한 상품 목록
    * 작성한 글 목록
    * 누적 사용 금액
    * 회원 등급
    * 팔로우/언팔로우
  * 회원 정보 수정



---

## :computer: 서비스 시연

![chickurl_시연]()





---

## :purple_heart: 프로젝트 후 느낀점
|팀원|느낀점|
|---|---|
|장영진|살짝 아쉽지만, 여태했던 프로젝트들과 비교해서 완성도 높은 프로젝트를 완성할 수 있었다. 자바스크립트를 얼른 숙련시켜 더 많이 활용하고 싶다. 아직 못한 부분이 있어 아쉽다. 생각보다 시간이 더 짧았다. 계획을 더 세세하게 나눠서 진행해야겠다.|
|이동현|시간이 좀 넉넉하지 않을까 생각했던 것은 완전 오산이었고.. 정말 순식간에 프로젝트의 막바지가 다가왔다는 느낌입니다. 자바스크립트쪽이 엄청난 부족함을 느꼇고.. 백엔드 개발자를 희망하는데 백엔드쪽의 실력도 정말 너무너무 턱없다는 것을 느꼇던 이번 프로젝트입니다.. 이번 2주의 프로젝트도 자기관리, 컨디션관리가 얼마나 중요한지를 깨달았습니다... 아프면.. 1일 2일정도는 순식간에 지나가버리고.. 지나간 시간을 다시 매꾸는것이 정말 쉽지 않았습니다. 컨디션 관리! 체력관리! 화이팅!|
|최보영|시간이 어떻게 흘렀는지 모르겠네요. 오류를 하나 고치면 다른 오류가 나고 그걸 고치면 다른 오류가 나고 그런데 이제 오류는 이곳저곳에서 터지질 않나, 자바스크립트는 되다 안되고 정말 정신이 없었습니다. 그래도 다같이 이슈를 해결하다 보니 이젠 저도 어엿한 이슈 킬러가 된 것 같네요. 취약했던 자바스크립트에 대해 더 많이 알게 된 것 같습니다. 문서 정리 방법과 다양한 이슈 해결 능력을 기를 수 있어 유익한 시간이 되었습니다. 그리고 엄청난 프론트엔드 스킬을 바로 옆에서 볼 수 있어 이렇게도 화면을 구성할 수 있구나 감탄했습니다. 아쉬운 점으로는, 어쨌든 기능이 돌아가는 것에 집중하다 보니 최적화에 신경을 못 썼다는 점을 꼽을 수 있을 것 같습니다. 그리고 치컬 팀과 헤어져야 한다는 것..? 고생도 많았지만 즐겁고 값진 시간이었습니다. 감사합니다! 파이팅!!|
|차화영|products app은 이전까지의 articles, accounts와 다르게 상품 정보와 각각의 후기, 문의 그리고 구매 기능까지 있어서 구현하기가 좀 더 어려웠는데, 팀원 분들의 도움을 받아 완성시킬 수 있어 좋았습니다. 이슈를 해결하는 것, 디자인 등 팀원 개개인의 스타일이나 자세가 다 달랐는데 함께하는 과정에서 많이 배웠습니다. 평일, 주말 할 거 없이 야근하는 열정..!! 기획을 나름 세부적으로 짠 것 같은데 역시 명확히 구현하려면 기획 단계에서 시간을 더 투자해야한다는 것을 다시 느꼈습니다. 이번 프로젝트를 발판 삼아 비동기를 좀 더 공부할 수 있음 좋겠네요..ㅎㅎ 질문왕과 함께 하느라 고생하셨습니다.|
|최정아|프로젝트 기획, 개발 과정을 팀원과 협업하면서 다양한 개발 지식을 배울 수 있었고 배우는 과정 속에서 디버깅을 해결하는 역량을 함양할 수 있었습니다. 그리고 협업하면서 페이지 간의 접점(코드의 연결된 부분)이 실제 쇼핑몰 사이트에 미치는 영향력을 알게 되었습니다. Django에 기반한 웹 서비스의 accounts app을 구현하면서 데이터베이스를 사용해야 하는 상황이 많았는데 프로필 페이지를 구현하는 과정 중에 팀원과의 소통을 통해 효율적이지 못한 코드를 발견하고 개선할 수 있었습니다. 무엇보다도 팀의 개발 과정에 함께 참여하고 아이디어를 공유하면서 README 및 Notion 문서화 역량 강화와 소통 능력을 향상시켰습니다.|



---


