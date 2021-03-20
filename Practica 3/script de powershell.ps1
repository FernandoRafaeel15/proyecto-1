function test{
   param(
   [int]$numero
   )
   While($numero -lt 100){
   if($numero -eq 98){
   
   Write-Host "escribir"   
   }
   Write-Host "xd"
   $numero++
   }

}


test 16