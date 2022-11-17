// 문의 삭제 비동기
function delete_inquiry(form, product_pk, inquiry_pk) {
  // preventDafault를 onsubmit에다 해줌
  
  axios({
    method: 'post',
    url: `/products/${product_pk}/inquiry/${inquiry_pk}/delete/`,
    headers: {'X-CSRFToken': csrfToken},
  })
  .then(response => {
    console.log(response.data.isDeleted)
    const inquiryTableRows = document.querySelectorAll(`.inquiry-${inquiry_pk}`)
    
    inquiryTableRows.forEach(row => {
      row.remove()
    })
  })
}

// 문의 생성 비동기
function create_inquiry(form, product_pk) {
  const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value
  // console.log(form)
  // form 정보는 html onsubmit에서 this로 넘겨줌
  
  // axios({
  //   method: 'post',
  //   url: `/products/${product_pk}/inquiry/`,
  //   headers: {'X-CSRFToken': csrfToken},
  //   data: new FormData(form)
  // })
  // .then(response => {
  //   console.log(response.data.isSuccess)
  // })
}