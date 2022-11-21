/* 1. 문의 삭제 비동기 */
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


/* 2. 문의 수정 비동기 */
function update_inquiry(form, product_pk, inquiry_pk) {
  const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value
  
  axios({
    method: 'post',
    url: `/products/${product_pk}/inquiry/${inquiry_pk}/update/`,
    headers: {'X-CSRFToken': csrfToken},
    data: new FormData(form)
  })
  .then(response => {
    const inquiryTitle = document.querySelector(`#inquiry-title-${inquiry_pk}`)
    const inquiryContent = document.querySelector(`#inquiry-content-${inquiry_pk}`)

    inquiryTitle.innerText = response.data.inquiryTitle
    inquiryContent.innerText = response.data.inquiryContent
  })
}


/* 3. 문의 생성 비동기 (실제 사용 X) */
function create_inquiry(form, product_pk) {
  const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value
  
  axios({
    method: 'post',
    url: `/products/${product_pk}/inquiry/`,
    headers: {'X-CSRFToken': csrfToken},
    data: new FormData(form)
  })
  .then(response => {
    const inquiryPk = response.data.inquiryPk
    const inquiryUser = response.data.inquiryUser
    const inquiryCreatedAt = response.data.inquiryCreatedAt
    const inquiryTitle = response.data.inquiryTitle
    const inquiryContent = response.data.inquiryContent
    const productImageUrl = response.data.productImageUrl
    const productName = response.data.productName
    const productContent = response.data.productContent

    console.log(inquiryPk, inquiryUser, inquiryCreatedAt)
    const inquiryTableBody = document.querySelector('#inquiryTableBody')

    inquiryTableBody.insertAdjacentHTML('afterbegin', `
      <tr class="inquiry-${inquiryPk}" data-bs-toggle="collapse" data-bs-target="#collapse-inquiry-${inquiryPk}" aria-expanded="false"
      style="vertical-align: middle;">
        <td id="inquiry-title-${inquiryPk}" class="inquiry_title" scope="row" style="width: 710px;" class="px-3">${inquiryTitle}</td>
        <td style="width: 100px;" class="text-center">${inquiryUser}</td>
        <td style="width: 100px;" class="text-center">${inquiryCreatedAt}</td>
        <td style="width: 100px;" class="text-center">-</td>
      </tr>
      
      <!-- 문의 내용 및 답변 Collapse -->
      <tr class="collapse inquiry-${inquiryPk}" id="collapse-inquiry-${inquiryPk}">
        <td colspan="4" class="text-bg-light px-3">
          <div>
            <div class="d-flex">
              <div class="me-3">Q.</div>
              <div id="inquiry-content-${inquiryPk}">${inquiryContent}</div>
            </div>
            <div>
              <!-- 문의글 수정 & 삭제 O (admin 답변 X, user 검사 if문 X) -->
              <div class="d-flex justify-content-end mt-3">
                <a href="" class="text-muted me-2" data-bs-toggle="modal" data-bs-target="#updateInquiry${inquiryPk}">수정</a>
                
                <form id="inquiry-delete-form-${inquiryPk}" onsubmit="event.preventDefault(); delete_inquiry(this, '${product_pk}', '${inquiryPk}')">
                  <input type="submit" class="btn-none text-muted" value="삭제">
                </form>
              </div>
  
              <!-- 문의 수정 모달 -->
              <div class="modal fade" id="updateInquiry${inquiryPk}" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-hidden="true">
                <div class="modal-dialog">
                  <div class="modal-content">
                    <div class="modal-header">
                      <h1 class="modal-title fs-5" id="staticBackdropLabel">상품 문의하기</h1>
                      <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
  
                    <div class="modal-body">
                      <div class="d-flex align-items-center mb-3">
                        <img src="${productImageUrl}" alt="" class="rounded-1" width="64px" height="64px">
                        <div class="ms-3">
                          <p class="fs-5 fw-bold mb-1">${productName}</p>
                          <p class="text-muted m-0">${productContent}</p>
                        </div>
                      </div>
  
                      <!-- 문의 수정 폼 -->
                      <form id="inquiry-update-form-${inquiryPk}" onsubmit="event.preventDefault(); update_inquiry(this, '${product_pk}, '${inquiryPk}')">
                        {% csrf_token %}
  
                        <!-- inquiry_form -->
                        <div class="mb-3">
                          <label class="form-label" for="id_title">제목</label>
                          <input type="text" name="title" maxlength="50" class="form-control" placeholder="제목" required id="id_title" value=${inquiryTitle}>
                        </div>
                        <div class="mb-3">
                          <label class="form-label" for="id_content">내용</label>
                          <textarea name="content" cols="40" rows="10" class="form-control" placeholder="내용" required id="id_content">${inquiryContent}</textarea>
                        </div>
  
                        <div class="text-center">
                          <button type="button" class="btn me-2" data-bs-dismiss="modal"
                            style="border:solid 1px #d3d3d3; border-radius:3px; height:50px; width:120px; background-color: white;">취소</button>
                          <button type="submit" class="btn" data-bs-dismiss="modal"
                            style="border-radius:3px; height:50px; width:120px; background-color: #5e0080; color: white">등록</button>
                        </div>
                      </form>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </td>
      </tr>
    `)

    form.reset()
  })
}


/* 4. 답글 생성 비동기 */
function create_reply(form, product_pk, inquiry_pk) {
  const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value
  console.log(form)

  axios({
    method: 'post',
    url: `/products/${product_pk}/inquiry/${inquiry_pk}/reply/`,
    headers: {'X-CSRFToken': csrfToken},
    data: new FormData(form)
  })
  .then(response => {
    const replyContent = response.data.replyContent
    const replyBox = document.querySelector(`#reply-box-${inquiry_pk}`)
    const updateDeleteBtns = document.querySelector(`#inquiry-update-delete-btns-${inquiry_pk}`)  // 문의 수정 삭제 버튼
    const hr = document.querySelector(`#inquiry-hr-${inquiry_pk}`)
    const replyStatus = document.querySelector(`#reply-status-${inquiry_pk}`)

    replyBox.classList.remove('d-none')
    replyBox.insertAdjacentHTML('afterbegin', `
      <div class="me-3">A.</div>
      <div class="text-break">${replyContent}</div>
    `)

    replyStatus.innerText = '답변완료'
    replyStatus.style.color = '#5e0080'

    hr.remove()
    form.remove()
    if (updateDeleteBtns) {
      updateDeleteBtns.remove()
    }
  })
}
