module MemoryModel(
                   input             clk,
                   input             rstn,
                   output reg        RVld,
                   input             RRdy,
                   input [31:0]      RAddr,
                   input [31:0]      RWData,
                   input             RWEn,
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
         RVld <= 0;
         if (RVld) begin
            RVld <= 0;
         end
         else if (RRdy) begin
            RVld <= 1;
         end
      end
   end
   
   wire [31:0] mem0x100;
   wire [31:0] mem0x101;
   wire [31:0] mem0x102;
   wire [31:0] mem0x103;
   wire [31:0] mem0x104;
   wire [31:0] mem0x105;
   wire [31:0] mem0x106;
   wire [31:0] mem0x107;
   wire [31:0] mem0x108;
   wire [31:0] mem0x109;

   assign mem0x100 = mem['h100];
   assign mem0x101 = mem['h101];
   assign mem0x102 = mem['h102];
   assign mem0x103 = mem['h103];
   assign mem0x104 = mem['h104];
   assign mem0x105 = mem['h105];
   assign mem0x106 = mem['h106];
   assign mem0x107 = mem['h107];
   assign mem0x108 = mem['h108];
   assign mem0x109 = mem['h109];

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
   wire        Halt;
   
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
      @(posedge clk);
      LEn <= 0;
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
      .LEn(LEn),
      .Halt(Halt));

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
      //file2mem("tstPattern0002.txt");
      //file2mem("tstPattern0003.txt");
      file2mem("outfiletstPattern0004.txt");
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
