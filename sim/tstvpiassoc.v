module test;
   reg [31:0] data;
   reg [31:0] address;
   initial begin
      address = 'hFFFFFFFF;
      //$dynmem_write(address,4);
      //
      //data = $dynmem_read(address);
      //$display("data after read: %0x", data);
      //
      //address = 'hABCDE123;
      //$dynmem_write(address,'h444444);
      //
      //data = $dynmem_read(address);
      //$display("data after read: %0x", data);
      //
      //$display("reading @00000888");
      //$display("%08x", $dynmem_read('h00000888));

      //+00000000 FFFFF237
      //+00000001 0000126F
      //+00000002 FFFFFFFF

      address = 'h00000000;
      data = 'hFFFFF237;
      $dynmem_write(address,data);
      address = 'h00000001;
      data = 'h0000126F;
      $dynmem_write(address,data);
      address = 'h00000002;
      data = 'hFFFFFFFF;
      $dynmem_write(address,data);
      $display("%08x", $dynmem_read('h00000000));
      $display("%08x", $dynmem_read('h00000001));
      $display("%08x", $dynmem_read('h00000002));
      $display("%08x", $dynmem_read('h00000003));
   end
endmodule
