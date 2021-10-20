$(document).ready(function () {
  $(document).on('mousemove', function (e) {
    const xPos = e.pageX;
    const yPos = e.pageY;
    // console.log(xPos, yPos);
    $('.circle-out').css({
      top: yPos - 12,
      left: xPos - 12
    });
  });

  $('a, button, input, select').hover(function () {
    $('.circle-out').addClass('active');
  }, function () {
    $('.circle-out').removeClass('active');
  });

  // $('.modal').modal('show')

  // $('#mymodal').modal();

  // function afterModalTransition (e) {
  //   e.setAttribute('style', 'display: none !important;');
  // }
  // $('#mymodal').on('hide.bs.modal', function () {
  //   setTimeout(() => afterModalTransition(this), 200);
  // });
});
