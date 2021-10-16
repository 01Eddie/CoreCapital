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

  $('a, button').hover(function () {
    $('.circle-out').addClass('active');
  }, function () {
    $('.circle-out').removeClass('active');
  });
});
