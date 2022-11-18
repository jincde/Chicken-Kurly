// 1. 결제 준비
IMP.init("imp74723253") // 가맹점 식별코드


// 2. 수량이 0이면 결제 버튼 비활성화
const btnPayment = document.querySelector('#btn-payment')
// const quantityField = document.querySelector('#id_quantity')

quantityField.addEventListener('input', event => {
  if (event.target.value === '0') {
    btnPayment.disabled = true
  } else {
    btnPayment.disabled = false
  }
})


// 3. 카카오페이 결제창 띄우기
function requestPay(product_pk, product_name) {
  const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value  
  const price = Number(document.querySelector('#price').innerText)
  
  const quantity = Number(quantityField.value)
  const productBuyForm = document.querySelector('#product-buy-form')
  let formData = new FormData(productBuyForm)

  IMP.request_pay({ // param
    pg: "kakaopay", // 카카오페이 결제창 호출
    pay_method: "card",
    merchant_uid: 'merchant_' + new Date().getTime(),
    name: product_name,
    amount: price * quantity,
  }, function (rsp) { // callback
    if (rsp.success) {
      formData.append('imp_uid', rsp.imp_uid)
      formData.append('merchant_uid', rsp.merchant_uid)

      axios({
        method: 'post',
        url: `/products/${product_pk}/payment/`,
        headers: {'X-CSRFToken': csrfToken},
        data: formData
      })
      .then(response => {
        
      })
    } else {
      // 결제 실패 시 로직,
      console.log("결제에 실패하였습니다. 에러 내용: " +  rsp.error_msg);
    }
  });
}