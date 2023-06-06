// 메뉴 스크롤링 시 고정
window.addEventListener("scroll", function() {
    var header = document.querySelector("header");
    header.classList.toggle("sticky", window.scrollY > 0);
  });
  
  // Smooth 스크롤
  document.querySelectorAll('a[href^="#"]').forEach(function(anchor) {
    anchor.addEventListener("click", function(e) {
      e.preventDefault();
      document.querySelector(this.getAttribute("href")).scrollIntoView({
        behavior: "smooth"
      });
    });
  });
  
  // 양식 제출 시 알림 메시지 표시
  var form = document.querySelector("form");
  form.addEventListener("submit", function(e) {
    e.preventDefault();
    alert("메시지가 성공적으로 전송되었습니다!");
    form.reset();
  });
  