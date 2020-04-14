Program one;
uses crt;
var a,b:Array [1..100,1..100] of integer;
g,i,n,j,s,s_minus:integer;
Begin
  writeln('^^^^^^^^^^^^^^^^START PROGRAMM^^^^^^^^^^^^^');
  writeln('введите кол во строк и столцов'); //было лень делать отдельно кол во столбцов и строк... извините... это вам не пайтон  
  read(n);
  writeln('--------------------------------------------------------------');
    For i:=1 to n do
      begin
      For j:=1 to n do
        begin
          writeln('введите число');
          read(a[i,j]);
        end;
      end;
      
    writeln('chek point_1-OK');
    
    i:=0;s:=0;g:=0;s_minus:=0;
    while i<=n do
      begin
      i:=i+1;
      j:=0;
      while j<=n do 
        begin
          j:=j+1;
          if(a[i,j]>0)then
          begin
            s:=s+a[i,j];
            g:=g+1;
          end;
          s_minus:=s_minus+a[i,j];
        end;
      end;
      
    writeln('chek point_2-OK');
    writeln('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%END_math%%%%%%%%%%%%%%%%%');
    if s=s_minus then 
    begin
      writeln('ВСЕ ЧИСЛА > 0');
      writeln('Количество: ',g);
      writeln('Сумма: ',s);
    end
    else
      begin
        writeln('Количество: ',g);
        writeln('Сумма БЕЗ "-": ',s);
        writeln('Сумма C "-": ',s_minus);
    end;
writeln('########################## END PROGRAMM #########################');   
end.
