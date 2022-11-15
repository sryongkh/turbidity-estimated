$(document).ready(function () {
  // Init
  $(".image-section").hide();
  $(".loader").hide();
  $("#result").hide();
  $("#userdata").hide();
  // Example pic
  function readURL(input) {
    if (input.files && input.files[0]) {
      var reader = new FileReader();
      reader.onload = function (e) {
        $("#imagePreview").css(
          "background-image",
          "url(" + e.target.result + ")"
        );
        $("#imagePreview").hide();
        $("#imagePreview").fadeIn(650);
      };
      reader.readAsDataURL(input.files[0]);
    }
  }
  $("#imageUpload").change(function () {
    $(".image-section").show();
    $("#btn-predict").show();
    $("#result").text("");
    $("#result").hide();
    $("#userdata").hide();
    $("#userdata tbody").children().last().remove();
    $("#result").children().last().remove();
    readURL(this);
  });
  // ประมาณค่า
  $("#btn-predict").click(function () {
    var form_data = new FormData($("#upload-file")[0]);
    $(this).hide();
    $(".loader").show();
    $.ajax({
      type: "POST",
      url: "/",
      data: form_data,
      contentType: false,
      cache: false,
      processData: false,
      async: true,
      /*error: function (xhr) {
        var err = eval("'(" + xhr.responseText + ")'");
        alert(err.Message);
      },*/
      success: function (data) {
        //Get and display the result
        $(".loader").hide();
        $("#userdata").fadeIn(600);
        $("#result").fadeIn(600);
        $("#result").text(" ประมาณค่าความขุ่นได้ : " + data + " NTU");
        var feature = [];
        $.getJSON("static/data/data.json", function (data) {
          $.each(data.feature, function (i, f) {
            var tblRow =
              "<tr>" +
              "<td>" +
              f.max_gry +
              "</td>" +
              "<td>" +
              f.min_gry +
              "</td>" +
              "<td>" +
              f.mean_gry +
              "</td>" +
              "<td>" +
              f.std_gry +
              "</td>" +
              "<td>" +
              f.mean_r +
              "</td>" +
              "<td>" +
              f.mean_g +
              "</td>" +
              "<td>" +
              f.mean_b +
              "</td>" +
              "<td>" +
              f.std_r +
              "</td>" +
              "<td>" +
              f.std_g +
              "</td>" +
              "<td>" +
              f.std_b +
              "</td>" +
              "<td>" +
              f.mean_lu +
              "</td>" +
              "<td>" +
              f.std_lu +
              "</td>" +
              "</tr>";
            $(tblRow).appendTo("#userdata tbody");

            //$(tblRow).appendTo("#userdata tbody");
          });
        });

        console.log("Success!");
      },
    });
  });
});
// table
$(window)
  .on("load resize ", function () {
    var scrollWidth =
      $(".tbl-content").width() - $(".tbl-content table").width();
    $(".tbl-header").css({ "padding-right": scrollWidth });
  })
  .resize();
