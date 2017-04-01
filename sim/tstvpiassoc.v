module test;
   reg [31:0] data;
   initial begin
      data = 'hFFFFFFFF;
      $dynmem_write(data,4);
   end
endmodule
