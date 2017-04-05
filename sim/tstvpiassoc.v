module test;
   reg [31:0] data;
   reg [31:0] address;
   initial begin
      address = 'hFFFFFFFF;
      $dynmem_write(address,4);

      data = $dynmem_read(address);
      $display("data after read: %0x", data);

      address = 'hABCDE123;
      $dynmem_write(address,'h444444);

      data = $dynmem_read(address);
      $display("data after read: %0x", data);

      $display("reading @00000888");
      $display("%08x", $dynmem_read('h00000888));
   end
endmodule
