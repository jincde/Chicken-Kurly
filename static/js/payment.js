// 1. 결제 준비
IMP.init("imp74723253") // 가맹점 식별코드

function requestPay() {
  const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value  
  const cartUpdateForm = document.querySelector('#cart-update-form')
  let formData = new FormData(cartUpdateForm)
  
  IMP.request_pay({ // param
    pg: "kakaopay", // 카카오페이 결제창 호출
    pay_method: "card",
    merchant_uid: 'merchant_' + new Date().getTime(),
    name: "노르웨이 회전 의자", // ㅇㅇㅇ외 몇 개 이렇게 할까
    amount: 100,
    buyer_email: "gildong@gmail.com",
    buyer_name: "홍길동",
    buyer_tel: "010-4242-4242",
    buyer_addr: "서울특별시 강남구 신사동",
    buyer_postcode: "01181"
  }, function (rsp) { // callback
    if (rsp.success) {
      axios({
        method: 'post',
        url: '/accounts/cart/payment/',
        headers: {'X-CSRFToken': csrfToken},
        data: formData
        // data: {
        //   'imp_uid': rsp.imp_uid,
        //   'merchant_uid': rsp.merchant_uid,
        //   'formData': formData
        // }
      })
      .then(response => {

      })
    } else {
      // 결제 실패 시 로직,
      alert("결제에 실패하였습니다. 에러 내용: " +  rsp.error_msg);
    }
      // if (rsp.success) {
      //     // 결제 성공 시 로직,
      //     // 결제 성공 시: 결제 승인 또는 가상계좌 발급에 성공한 경우
      //     // jQuery로 HTTP 요청
      //     jQuery.ajax({
      //       url: "/accounts/cart/payment/", // 예: https://www.myservice.com/payments/complete
      //       method: "POST",
      //       headers: { "Content-Type": "application/json" },
      //       data: {
      //         imp_uid: rsp.imp_uid,
      //         merchant_uid: rsp.merchant_uid,
      //       }
      //   }).done(function (data) {
      //     // 가맹점 서버 결제 API 성공시 로직
      // })
      // } else {
      //     // 결제 실패 시 로직,
      //     alert("결제에 실패하였습니다. 에러 내용: " +  rsp.error_msg);
      // }
  });
}