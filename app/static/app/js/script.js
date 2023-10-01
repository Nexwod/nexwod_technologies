


$(".plus-cart").click(function()
{
    var id = $(this).attr("pid").toString();
var cal = this.parentNode.children[2]
console.log("pid=", id)
$.ajax({
    type: "GET",
    url : "/pluscart",
    data:{
        prod_id:id
    },
    success:function(data){
        console.log("data =", data);
        cal.innerText=data.quantity
        document.getElementById('amount').innerText=data.amount
        document.getElementById("totalamount").innerText=data.totalamount

    }
})
     
})

$(".remove-cart").click(function()
{
   var id =$(this).attr('pid').toString();
   var cal = this

   $.ajax({
       type:"GET",
       url:"/removecart",
       data:{prod_id:id},
       success:function(data){
           document.getElementById("amount").innerText=data.amount
           document.getElementById("totalamount").innerText=data.totalamount
           cal.parentNode.parentNode.parentNode.parentNode.remove()
       }
   })
   
})

$(".minus-cart").click(function()
{
   var id =$(this).attr('pid').toString();
   var cal = (this.parentNode.children[2]);

   $.ajax({
       type:"GET",
       url:"/minuscart",
       data:{prod_id:id},
       success:function(data){
           cal.innerText=data.quantity
           document.getElementById("amount").innerText=data.amount
           document.getElementById("totalamount").innerText=data.totalamount
       }
   })
   
})


