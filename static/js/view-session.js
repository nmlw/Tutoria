var status_badge = {
    "Booked":'<h6 class="card-subtitle mb-2 text-muted"><span class="badge badge-info">Booked</span></h6>',
    "Committed": '<h6 class="card-subtitle mb-2 text-muted"><span class="badge badge-warning">Committed</span></h6>',
    "Finished": '<h6 class="card-subtitle mb-2 text-muted"><span class="badge badge-dark">Finished</span></h6>',
    "Canceled": '<h6 class="card-subtitle mb-2 text-muted"><span class="badge badge-danger">Canceled</span></h6>'
};

$(document).ready(function(){
    // console.log($(".card-title").attr("status"));
    $(".card-title").after(status_badge[$(".card-title").attr("status")]);
    
    $(".session-cancel-btn").click(function(){
        window.location = "/canceling/"+$(this).parent().attr("sessionId");
    });
});