$(()=>{

console.log('I am ready');


$('#ratingModal').on('show.bs.modal', event => {
  var button = $(event.relatedTarget);
  var modal = $(this);

  
  
});
$('#voteform').submit((e)=>{
    e.preventDefault()
    form=$('#voteform')
    project=$('#targetproject').val()

    design_rating=$('input[name=designoptions]:checked')
    console.log(design_rating.val())
    $.ajax({
      'url':`/project/${project}/vote`,
      'type':'POST',
      'data':form.serialize(),
      'dataType':'json',
      'success':(data)=>{alert(data['success'])},
    })
    $('#ratingModal').modal('hide');
   return false;
  });


});