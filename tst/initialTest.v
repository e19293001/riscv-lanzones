//`ifdef FIXRESPONSE
//module MemoryModel(
//                   input             clk,
//                   input             rstn,
//                   output 		       RVld,
//                   input             RRdy,
//                   input [31:0]      RAddr,
//                   input [31:0]      RWData,
//                   input             RWEn,
//                   input [3:0] 		 RWStrobe,
//                   output [31:0] RData
//                   );
//
//   reg [31:0] mem ['hFFFFFFF:0];
//
//   wire [31:0] strb_w;
//
//   assign strb_w = {{8{RWStrobe[3]}},{8{RWStrobe[2]}},{8{RWStrobe[1]}},{8{RWStrobe[0]}}};
//   
//   always @(posedge clk) begin
//      if (RWEn) begin
//         //mem[RAddr] <= RWData;
//         mem[RAddr] <= (mem[RAddr] & ~strb_w) | (RWData & strb_w);
//      end
//   end
//
//   assign RData = (RRdy && RVld) ? mem[RAddr] : 0;
//
////   assign RVld = RRdy;
//   assign RVld = 1;
////   always @(posedge clk) begin
////      if (!rstn) begin
////         RVld <= 0;
////      end
////      else begin
////         RVld <= 0;
////         if (RVld) begin
////            RVld <= 0;
////         end
////         else if (RRdy) begin
////            RVld <= 1;
////         end
////      end
////   end
//
//   wire [31:0] mem0x100;
//   wire [31:0] mem0x101;
//   wire [31:0] mem0x102;
//   wire [31:0] mem0x103;
//   wire [31:0] mem0x104;
//   wire [31:0] mem0x105;
//   wire [31:0] mem0x106;
//   wire [31:0] mem0x107;
//   wire [31:0] mem0x108;
//   wire [31:0] mem0x109;
//
//   wire [31:0] mem0x000;
//   wire [31:0] mem0x001;
//   wire [31:0] mem0x002;
//   wire [31:0] mem0x003;
//   wire [31:0] mem0x004;
//   wire [31:0] mem0x005;
//   wire [31:0] mem0x006;
//   wire [31:0] mem0x007;
//   wire [31:0] mem0x008;
//   wire [31:0] mem0x009;
//
//   wire [31:0] mem0x010;
//   wire [31:0] mem0x011;
//   wire [31:0] mem0x012;
//   wire [31:0] mem0x013;
//   wire [31:0] mem0x014;
//   wire [31:0] mem0x015;
//   wire [31:0] mem0x016;
//   wire [31:0] mem0x017;
//   wire [31:0] mem0x018;
//   wire [31:0] mem0x019;
//
//   assign mem0x100 = mem['h100];
//   assign mem0x101 = mem['h101];
//   assign mem0x102 = mem['h102];
//   assign mem0x103 = mem['h103];
//   assign mem0x104 = mem['h104];
//   assign mem0x105 = mem['h105];
//   assign mem0x106 = mem['h106];
//   assign mem0x107 = mem['h107];
//   assign mem0x108 = mem['h108];
//   assign mem0x109 = mem['h109];
//
//   assign mem0x000 = mem['h000];
//   assign mem0x001 = mem['h001];
//   assign mem0x002 = mem['h002];
//   assign mem0x003 = mem['h003];
//   assign mem0x004 = mem['h004];
//   assign mem0x005 = mem['h005];
//   assign mem0x006 = mem['h006];
//   assign mem0x007 = mem['h007];
//   assign mem0x008 = mem['h008];
//   assign mem0x009 = mem['h009];
//
//   assign mem0x010 = mem['h010];
//   assign mem0x011 = mem['h011];
//   assign mem0x012 = mem['h012];
//   assign mem0x013 = mem['h013];
//   assign mem0x014 = mem['h014];
//   assign mem0x015 = mem['h015];
//   assign mem0x016 = mem['h016];
//   assign mem0x017 = mem['h017];
//   assign mem0x018 = mem['h018];
//   assign mem0x019 = mem['h019];
//
//endmodule
//`else
module MemoryModel(
                   input             clk,
                   input             rstn,
                   output reg	       RVld,
                   input             RRdy,
                   input [31:0]      RAddr,
                   input [31:0]      RWData,
                   input             RWEn,
                   input [3:0] 		 RWStrobe,
                   output reg [31:0] RData
                   );

//   reg [31:0] mem [0:'hFFFF];

   reg [31:0] data;
   wire [31:0] strb_w;

   assign strb_w = {{8{RWStrobe[3]}},{8{RWStrobe[2]}},{8{RWStrobe[1]}},{8{RWStrobe[0]}}};
   
   always @(posedge clk) begin
      if (!rstn) begin
         RData <= 0;
      end
      else begin
         if (RWEn) begin
            data = $dynmem_read(RAddr);
            $dynmem_write(RAddr,((data & ~strb_w) | (RWData & strb_w)));
         end
         else begin
            if (RRdy && !RVld) begin
               //data = $dynmem_read(RAddr);
               //RData <= data;
               //$display("reading @RAddr: %08X\n", RAddr);
               RData <= $dynmem_read(RAddr);
               $display("reading from address: %08x data: %08x", RAddr, $dynmem_read(RAddr));
               //$display("RData: %08X\n", RData);
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

endmodule
//`endif

module initialTest;
   reg 			clk;
   reg 			rstn;
   wire 			RVld;
   wire [31:0] RData;
   wire [31:0]  RWData;
   wire [3:0]   RWStrobe;
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

   initial begin
      @(posedge clk);
      @(posedge rstn);
      @(posedge Halt);
      repeat (30) @(posedge clk);
      $display("@%0t: Halt detected", $time);
      $finish;
   end

   // PC register must be 4-byte aligned
   initial begin
      @(posedge clk);
      @(posedge rstn);
      forever begin
         @(posedge clk);
         if (dut.PCff[1:0] != 2'b0) begin
            $display("assertion failed. dut.PCff[1:0] is not zero.");
            $display("         value is: %08X", dut.PCff);
            repeat (3) @(posedge clk);
            $finish;
         end
      end
   end

   lanzones dut(
      .clk(clk),
      .rstn(rstn),
      .RVld(RVld),
      .RData(RData),
      .RWData(RWData),
      .RRdy(RRdy),
      .RWEn(RWEn),
      .RWStrobe(RWStrobe),
      .RAddr(RAddr),
      .LEn(LEn),
      .Halt(Halt));

   MemoryModel mem(
                   .clk(clk),
                   .rstn(rstn),
                   .RVld(RVld),
                   .RRdy(RRdy),
                   .RWStrobe(RWStrobe),
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
      //file2mem("outfiletstPattern0004.txt");
      //file2mem("outfiletstADD.txt");
      file2mem("outfile.txt");
   end
   
   task file2mem(input [8*128:1] str);
      integer fp;
      integer code;
      reg [31:0] indx; // should be an integer. but iverilog won't display %04x properly
      integer data;

      reg [8*128:1] datastr;
      integer       addrOrData;
      reg [8*128:1] tomem;
      reg [31:0]       addr0;
      reg [31:0]    datain;
      begin
         fp = $fopen(str, "r");
         $display("input file: %0s", str);
         if (fp == 0) begin
            $display("failed to open file: %0s", str);
            $finish();
         end

         code = 1;
         indx = 0;
         addrOrData = 0;
         while (code > 0) begin
            code = $fscanf(fp, "+%08x %08x\n", addr0, datain);
            //$display("code: %0d addr: %04x datain: %04x", code, addr, datain);

            //if (code > 0) begin
            //   $display("code: %0d addr: %08x datain: %08x", code, addr0, datain);
            //end

            if (code == 0) begin
               $display("invalid input code: %0d addr: %08x datain: %08x", code, addr0, datain);
               $finish;
            end
            $dynmem_write(addr0,datain);
//            $display("mem[%08x]: %08x", addr0, $dynmem_read(addr0));
            
            indx = indx + 1;
         end
         $fclose(fp);
         
//         $display("reading @00000888");
//         $display("%08x", $dynmem_read('h00000888));
//         mem.mem['h12345678] = 12345;
//         $display("mem.mem['h12345678]: %08x", mem.mem['h12345678]);
//         code = indx - 1;
//         $display("code: %0d indx: %0d\n", code, indx);
//         for (indx = 0; indx < code; indx = indx + 1) begin
////            $display("mem[%04x]: %04x", indx, mem.mem[indx]);
//            $display("mem[%04X]: %04X", indx, mem.mem[indx]);
//         end
      end
   endtask

endmodule
