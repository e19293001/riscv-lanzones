module MemoryModel(
                   input             clk,
                   input             rstn,
                   output reg        RVld,
                   input             RRdy,
                   input [31:0]      RAddr,
                   output reg [31:0] RData
                   );

   reg [31:0] mem ['hFFFF:0];

   always @(posedge clk) begin
      if (!rstn) begin
         RData <= 0;
      end
      else begin
         if (RRdy && !RVld) begin
            RData <= mem[RAddr];
         end
         else begin
            RData <= 0;
         end
      end
   end

   always @(posedge clk) begin
      if (!rstn) begin
         RVld <= 0;
      end
      else begin
         if (RVld) begin
            RVld <= 0;
         end
         else if (RRdy) begin
            RVld <= 1;
         end
      end
   end
endmodule

module initialTest;
   reg 			clk;
   reg 			rstn;
   wire 			RVld;
   wire [31:0] RData;
   wire        RRdy;
   wire [31:0] RAddr;
   reg         LEn;
   
   initial begin
      clk = 0;
      forever begin
         #1 clk = !clk;
      end
   end

   initial begin
      LEn <= 0;
      rstn = 1;
      repeat (3) @(posedge clk);
      rstn <= 0;
      repeat (3) @(posedge clk);
      rstn <= 1;

      repeat (3) @(posedge clk);
      LEn <= 1;
   end

   initial begin
      repeat (1000) @(posedge clk);
      $finish;
   end

   initial begin
	   $dumpfile("sim.vcd");
	   $dumpvars(-1, dut, mem);
   end

   lanzones dut(
      .clk(clk),
      .rstn(rstn),
      .RVld(RVld),
      .RData(RData),
      .RRdy(RRdy),
      .RAddr(RAddr),
      .LEn(LEn));

   MemoryModel mem(
                   .clk(clk),
                   .rstn(rstn),
                   .RVld(RVld),
                   .RRdy(RRdy),
                   .RAddr(RAddr),
                   .RData(RData)
                   );

   initial begin
      //file2mem("lwPattern.txt");
      file2mem("tstPattern0000.txt");
   end
   
   task file2mem(input [8*128:1] str);
      integer fp;
      integer code;
      reg [31:0] indx; // should be an integer. but iverilog won't display %04x properly
      integer data;

      reg [8*128:1] datastr;
      integer       addrOrData;
      reg [8*128:1] tomem;
      reg [31:0]    addr;
      reg [31:0]    datain;
      begin
         fp = $fopen(str, "r");
         $display("str: %0s", str);
         if (fp == 0) begin
            $display("failed to open file: %0s", str);
            $finish();
         end
         $display("file opened.");

         code = 1;
         indx = 0;
         addrOrData = 0;
         while (code > 0) begin
            code = $fscanf(fp, "+%08x %08x\n", addr, datain);
            //$display("code: %0d addr: %04x datain: %04x", code, addr, datain);
            $display("code: %0d addr: %0d datain: %08x", code, addr, datain);
            if (code == 0) begin
               $display("invalid input code: %0d addr: %0d datain: %08x", code, addr, datain);
               $finish;
            end
            mem.mem[addr] = datain;
            indx = indx + 1;
         end
         $fclose(fp);
         code = indx - 1;
         $display("code: %0d indx: %0d\n", code, indx);
         for (indx = 0; indx < code; indx = indx + 1) begin
//            $display("mem[%04x]: %04x", indx, mem.mem[indx]);
            $display("mem[%0d]: %04x", indx, mem.mem[indx]);
         end
      end
   endtask

endmodule
