module MemoryModel(
                   input             clk,
                   input             rstn,
                   output reg        RVld,
                   input             RRdy,
                   input [31:0]      RAddr,
                   input [31:0]      RWData,
                   input 				 RWEn,
                   output reg [31:0] RData
                   );

   reg [31:0] mem ['hFFFF:0];

   always @(posedge clk) begin
      if (!rstn) begin
         RData <= 0;
      end
      else begin
         if (RWEn) begin
            mem[RAddr] <= RWData;
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

   wire [31:0] mem00;
   wire [31:0] mem01;
   wire [31:0] mem02;
   wire [31:0] mem03;
   wire [31:0] mem04;
   wire [31:0] mem05;
   wire [31:0] mem06;
   wire [31:0] mem07;
   wire [31:0] mem08;
   wire [31:0] mem09;

   assign mem00 = mem[00];
   assign mem01 = mem[01];
   assign mem02 = mem[02];
   assign mem03 = mem[03];
   assign mem04 = mem[04];
   assign mem05 = mem[05];
   assign mem06 = mem[06];
   assign mem07 = mem[07];
   assign mem08 = mem[08];
   assign mem09 = mem[09];

endmodule

module initialTest;
   reg 			clk;
   reg 			rstn;
   wire 			RVld;
   wire [31:0] RData;
   wire [31:0]  RWData;
   wire        RRdy;
   wire [31:0] RAddr;
   reg         LEn;
   wire        RWEn;
   
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
	   $dumpvars(-1, dut, mem, initialTest);
   end

   lanzones dut(
      .clk(clk),
      .rstn(rstn),
      .RVld(RVld),
      .RData(RData),
      .RWData(RWData),
      .RRdy(RRdy),
      .RWEn(RWEn),
      .RAddr(RAddr),
      .LEn(LEn));

   MemoryModel mem(
                   .clk(clk),
                   .rstn(rstn),
                   .RVld(RVld),
                   .RRdy(RRdy),
                   .RAddr(RAddr),
                   .RWData(RWData),
                   .RWEn(RWEn),
                   .RData(RData)
                   );

   initial begin
      //file2mem("lwPattern.txt");
      //file2mem("tstPattern0000.txt");
      //file2mem("tstPattern0001.txt");
      file2mem("tstPattern0002.txt");
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
