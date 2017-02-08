module lanzones(
                input         clk,
                input         rstn,
                input         RVld,
                input [31:0]  RData,
                output [31:0] RWData,
                output        RWEn,
                output        RRdy,
                output [31:0] RAddr,
                output        Halt,
                input         LEn
                );

   reg                 RRdy;
   reg [31:0]          RAddr;
   reg                 RWEn;
   reg [31:0]          RWData;

   reg                 Halt;

   reg [31:0]          FIff;
   reg [31:0]          DIff;
   reg [31:0]          EXff;
   reg [31:0]          MAff;
   reg [31:0]          WBff;

   reg [31:0]          PCff;

   wire                FIctrl;
   reg                 DIctrlff;
   wire                EXctrl;
   wire                MActrl;
   wire                WBctrl;

   wire                PCctrl;

   reg [31:0]          x0ff;
   reg [31:0]          x1ff;
   reg [31:0]          x2ff;
   reg [31:0]          x3ff;
   reg [31:0]          x4ff;
   reg [31:0]          x5ff;
   reg [31:0]          x6ff;
   reg [31:0]          x7ff;
   reg [31:0]          x8ff;
   reg [31:0]          x9ff;
   reg [31:0]          x10ff;
   reg [31:0]          x11ff;
   reg [31:0]          x12ff;
   reg [31:0]          x13ff;
   reg [31:0]          x14ff;
   reg [31:0]          x15ff;
   reg [31:0]          x16ff;
   reg [31:0]          x17ff;
   reg [31:0]          x18ff;
   reg [31:0]          x19ff;
   reg [31:0]          x20ff;
   reg [31:0]          x21ff;
   reg [31:0]          x22ff;
   reg [31:0]          x23ff;
   reg [31:0]          x24ff;
   reg [31:0]          x25ff;
   reg [31:0]          x26ff;
   reg [31:0]          x27ff;
   reg [31:0]          x28ff;
   reg [31:0]          x29ff;
   reg [31:0]          x30ff;
   reg [31:0]          x31ff;

   reg [4:0]           xAddr;
   reg [31:0]          xWData;
   reg 		 	        xWEn;

   wire [6:0]  opcode_instw;

   reg [4:0]   rd_ctrl;
   reg [4:0]   rdff;
   reg [19:0]  imm_ctrl;

   reg         DI_LUI_ctrl;
   reg         DI_ADD_ctrl;
   reg         DI_SUB_ctrl;
   reg         DI_SLL_ctrl;
   reg         DI_SW_ctrl;

   reg         DI_ORI_ctrl;
   reg         DI_ANDI_ctrl;
   reg         DI_ADDI_ctrl;
   reg         DI_SLLI_ctrl;
   reg         DI_SRLI_ctrl;
   reg         DI_SRAI_ctrl;

   reg         DI_LW_ctrl;
   reg         DI_LW_LHff;
   wire        DI_LW_w;
   wire        DI_LW_LHxW_ctrl;

   reg         DI_LH_ctrl;

   reg [6:0]   funct7_ctrl;
   reg [4:0]   rs1_ctrl;
   reg [4:0]   rs2_ctrl;
   reg [2:0]   funct3_ctrl;

   reg [31:0]  alu_outctrl;

   reg                 stallctrl;
   reg                 stallff;
   wire                fetchctrl;

   assign FIctrl = (RRdy & RVld) ? 1 : 0;
   //assign DIctrl = 1;
   assign EXctrl = 1;
   assign MActrl = 1;
   assign WBctrl = 1;

   assign fetchctrl = stallff ? 0 : 1;

   assign DI_LW_w = (DI_LW_ctrl | DI_LW_LHff) ? 1 : 0;
   assign DI_LW_LHxW_ctrl = (DI_LW_LHff & RVld) ? 1 : 0;

   always @(posedge clk) begin
      if (!rstn) begin
         rdff <= 0;
      end
      else begin
         if (DI_LW_ctrl || DI_LH_ctrl) begin
            rdff = rd_ctrl;
         end
      end
   end
   
   always @(posedge clk) begin
      if (!rstn) begin
         DI_LW_LHff <= 0;
      end
      else begin
         if (DI_LW_ctrl | DI_LH_ctrl) begin
            DI_LW_LHff <= 1;
         end
         else if (DI_LW_LHff && RVld) begin
            DI_LW_LHff <= 0;
         end
      end
   end

   always @(posedge clk) begin
      if (!rstn) begin
         Halt <= 1;
      end
      else begin
         if (LEn) begin
            Halt <= 0;
         end
         else if (opcode_instw == 7'h7F) begin
            Halt <= 1;
         end
      end
   end

   always @(posedge clk) begin
      if (!rstn) begin
         DIctrlff <= 0;
      end
      else begin
         if (FIctrl) begin
            DIctrlff <= 1;
         end
         else begin
            DIctrlff <= 0;
         end
      end
   end
   
   always @(posedge clk) begin
      if (!rstn) begin
         RRdy <= 0;
      end
      else begin
         if (!Halt) begin
            if (RVld) begin
               RRdy <= 0;
            end
            else begin
               RRdy <= 1;
            end
         end
         else begin
            RRdy <= 0;
         end
      end
   end

   always @(posedge clk) begin
      if (!rstn) begin
         RWEn <= 0;
      end
      else begin
         if (!Halt) begin
            if (stallctrl && DI_SW_ctrl) begin
               RWEn <= 1;
            end
            else if (RVld) begin
               RWEn <= 0;
            end
         end
      end
   end

   always @(posedge clk) begin
      if (!rstn) begin
         RWData <= 0;
      end
      else begin
         if (!Halt) begin
            if (stallctrl && DI_SW_ctrl) begin
               RWData <= xRData1;
            end
            else if (RVld) begin
               RWData <= 0;
            end
         end
      end
   end

   always @(posedge clk) begin
      if (!rstn) begin
         stallff <= 0;
      end
      else begin
         if (stallctrl) begin
            stallff <= 1;
         end
         else if (stallff && RVld) begin
            stallff <= 0;
         end
      end
   end

   assign PCctrl = stallff ? 0 : 1;
   
   always @(posedge clk) begin
      if (!rstn) begin
         PCff <= 0;
      end
      else begin
         if (RVld) begin
            if (PCctrl) begin
               PCff <= PCff + 1;
            end
         end
      end
   end

   always @(posedge clk) begin
      if (!rstn) begin
         RAddr <= 0;
      end
      else begin
         if (!Halt) begin
            if (stallctrl) begin
               RAddr <= alu_outctrl;
            end
            else begin
               if (fetchctrl) begin
                  RAddr <= PCff;
               end
               else if (RVld) begin
                  RAddr <= 0;
               end
            end
         end
      end
   end

   always @(posedge clk) begin
      if (!rstn) begin
         FIff <= 0;
      end
      else begin
         if (FIctrl) begin
            FIff <= RData;
         end
      end
   end

   assign opcode_instw = FIff[6:0];

   // instruction decoder
   always @* begin
      DI_LUI_ctrl = 0;
      DI_ADD_ctrl = 0;
      DI_SUB_ctrl = 0;
      DI_SLL_ctrl = 0;
      DI_SW_ctrl = 0;
      DI_LW_ctrl = 0;
      DI_LH_ctrl = 0;

      DI_ORI_ctrl = 0;
      DI_ANDI_ctrl = 0;
      DI_ADDI_ctrl = 0;
      DI_SLLI_ctrl = 0;
      DI_SRLI_ctrl = 0;
      DI_SRAI_ctrl = 0;

      rd_ctrl = 0;
      imm_ctrl = 0;
      funct7_ctrl = 0;
      funct3_ctrl = 0;
      rs1_ctrl = 0;
      rs2_ctrl = 0;
      stallctrl = 0;
      
      if (DIctrlff) begin
         case (opcode_instw)
           7'b0010011: begin
              case (FIff[14:12])
                3'b000: DI_ADDI_ctrl = 1;
                3'b001: DI_SLLI_ctrl = 1;
                3'b101: begin
                   if (FIff[31:25] == 7'b0000000) begin
                      DI_SRLI_ctrl = 1;
                   end
                   else if (FIff[31:25] == 7'b0100000) begin
                      DI_SRAI_ctrl = 1;
                   end
                   else begin
                      DI_SRLI_ctrl = 1; // WARNING: should throw an error for invalid instruction
                   end
                end
                3'b110: DI_ORI_ctrl = 1;
                3'b111: DI_ANDI_ctrl = 1;
                default: DI_ORI_ctrl = 1; // WARNING: should throw an error for unknown funct3
              endcase
              imm_ctrl = {7'b0,FIff[24:20]};
              rs1_ctrl = FIff[19:15];
              funct3_ctrl = FIff[14:12];
              rd_ctrl = FIff[11:7];
           end
           7'b0110111: begin // LUI
              DI_LUI_ctrl = 1;
              rd_ctrl = FIff[11:7];
              imm_ctrl = FIff[31:12];
           end
           7'b0110011: begin // ADD
              case (FIff[31:25])
                7'b0000000: begin
                   case (FIff[14:12])
                     3'b000: DI_ADD_ctrl = 1;
                     3'b001: DI_SLL_ctrl = 1;
                     default: DI_ADD_ctrl = 1; // WARNING: should throw an error for unknown funct3
                   endcase
                end
                7'b0100000: DI_SUB_ctrl = 1;
                default: DI_ADD_ctrl = 1; // WARNING: should throw an error for unknown funct7 
              endcase
              funct7_ctrl = FIff[31:25];
              rs2_ctrl = FIff[24:20];
              rs1_ctrl = FIff[19:15];
              funct3_ctrl = FIff[14:12];
              rd_ctrl = FIff[11:7];
           end
           7'b0100011: begin // SW
              DI_SW_ctrl = 1;
              imm_ctrl = {FIff[31:25],FIff[11:7]};
              rs2_ctrl = FIff[24:20];
              rs1_ctrl = FIff[19:15];
              funct3_ctrl = FIff[14:12];
              stallctrl = 1; // stop the fetch to write to memory
           end
           7'b0000011: begin // LW
              case (FIff[14:12])
                3'b010: DI_LW_ctrl = 1;
                3'b001: DI_LH_ctrl = 1;
                default: DI_LW_ctrl = 1; // WARNING: should throw an error for unknown funct3_ctrl
              endcase
              imm_ctrl = FIff[31:20];
              rs1_ctrl = FIff[19:15];
              funct3_ctrl = FIff[14:12];
              rd_ctrl = FIff[11:7];
              stallctrl = 1; // stop the fetch to read from memory
           end
         endcase
      end
   end

   // ALU
   always @* begin
      alu_outctrl = 0;
      if (DI_ADD_ctrl) begin
         alu_outctrl = xRData0 + xRData1;
      end
      else if (DI_SUB_ctrl) begin
         alu_outctrl = xRData0 - xRData1;
      end
      else if (DI_SLL_ctrl) begin
         alu_outctrl = xRData0 << xRData1;
      end
      else if (DI_SW_ctrl | DI_LW_ctrl) begin
         alu_outctrl = xRData0 + imm_ctrl;
      end
      else if (DI_LH_ctrl) begin
         alu_outctrl = xRData0[16:0] + imm_ctrl;
      end
      else if (DI_ORI_ctrl) begin
         alu_outctrl = xRData0 | imm_ctrl;
      end
      else if (DI_ANDI_ctrl) begin
         alu_outctrl = xRData0 & imm_ctrl;
      end
      else if (DI_ADDI_ctrl) begin
         alu_outctrl = xRData0 + imm_ctrl;
      end
      else if (DI_SLLI_ctrl) begin
         alu_outctrl = xRData0 << imm_ctrl;
      end
      else if (DI_SRLI_ctrl) begin
         alu_outctrl = xRData0 >> imm_ctrl;
      end
      else if (DI_SRAI_ctrl) begin
         alu_outctrl = $signed(xRData0) >>> imm_ctrl;
      end
   end

   // x register controller
   always @(posedge clk) begin
      if (!rstn) begin
         xWEn <= 0;
      end
      else begin
         if (DI_LUI_ctrl || 
             DI_ADD_ctrl || 
             DI_SUB_ctrl || 
             DI_SLL_ctrl ||
             DI_ORI_ctrl ||
             DI_ANDI_ctrl ||
             DI_ADDI_ctrl ||
             DI_SLLI_ctrl ||
             DI_SRLI_ctrl ||
             DI_SRAI_ctrl ||
             DI_LW_LHxW_ctrl) begin
            xWEn <= 1;
         end
         else begin
            xWEn <= 0;
         end
      end
   end

   always @(posedge clk) begin
      if (!rstn) begin
         xWData <= 0;
      end
      else begin
         if (DI_LUI_ctrl) begin
            xWData <= {imm_ctrl,12'h0};
         end
         else if (DI_ADD_ctrl ||
                  DI_SUB_ctrl ||
                  DI_SLL_ctrl ||
                  DI_ANDI_ctrl ||
                  DI_ADDI_ctrl ||
                  DI_SLLI_ctrl ||
                  DI_SRLI_ctrl ||
                  DI_SRAI_ctrl ||
                  DI_ORI_ctrl) begin
            xWData <= alu_outctrl;
         end
         else if (DI_LW_LHxW_ctrl) begin
            xWData <= RData;
         end
         else begin
            xWData <= 0;
         end
      end
   end

   always @(posedge clk) begin
      if (!rstn) begin
         xAddr <= 0;
      end
      else begin
         if (DI_LUI_ctrl) begin
            xAddr <= rd_ctrl;
         end
         else if (DI_ADD_ctrl || 
                  DI_SUB_ctrl ||
                  DI_SLL_ctrl ||
                  DI_ANDI_ctrl ||
                  DI_ADDI_ctrl ||
                  DI_SLLI_ctrl ||
                  DI_SRLI_ctrl ||
                  DI_SRAI_ctrl ||
                  DI_ORI_ctrl) begin
            xAddr <= rd_ctrl;
         end
         else if (DI_SW_ctrl) begin
            xAddr <= rs2_ctrl;
         end
         else if (DI_LW_LHxW_ctrl) begin
            xAddr <= rdff;
         end
         else begin
            xAddr <= 0;
         end
      end
   end
 
   always @(posedge clk) begin
      if (!rstn) begin
         DIff <= 0;
      end
      else begin
         if (DIctrlff) begin
            DIff <= FIff;
         end
      end
   end

   always @(posedge clk) begin
      if (!rstn) begin
         EXff <= 0;
      end
      else begin
         if (EXctrl) begin
            EXff <= DIff;
         end
      end
   end

   always @(posedge clk) begin
      if (!rstn) begin
         MAff <= 0;
      end
      else begin
         if (MActrl) begin
            MAff <= EXff;
         end
      end
   end

   always @(posedge clk) begin
      if (!rstn) begin
         WBff <= 0;
      end
      else begin
         if (WBctrl) begin
            WBff <= MAff;
         end
      end
   end

// register file
   reg [31:0] xRData0;
   always @* begin
      case (rs1_ctrl)
        0: xRData0 = x0ff;
        1: xRData0 = x1ff;
        2: xRData0 = x2ff;
        3: xRData0 = x3ff;
        4: xRData0 = x4ff;
        5: xRData0 = x5ff;
        6: xRData0 = x6ff;
        7: xRData0 = x7ff;
        8: xRData0 = x8ff;
        9: xRData0 = x9ff;
        10: xRData0 = x10ff;
        11: xRData0 = x11ff;
        12: xRData0 = x12ff;
        13: xRData0 = x13ff;
        14: xRData0 = x14ff;
        15: xRData0 = x15ff;
        16: xRData0 = x16ff;
        17: xRData0 = x17ff;
        18: xRData0 = x18ff;
        19: xRData0 = x19ff;
        20: xRData0 = x20ff;
        21: xRData0 = x21ff;
        22: xRData0 = x22ff;
        23: xRData0 = x23ff;
        24: xRData0 = x24ff;
        25: xRData0 = x25ff;
        26: xRData0 = x26ff;
        27: xRData0 = x27ff;
        28: xRData0 = x28ff;
        29: xRData0 = x29ff;
        30: xRData0 = x30ff;
        31: xRData0 = x31ff;
        default: xRData0 = 0;
      endcase
   end

   reg [31:0] xRData1;
   always @* begin
      case (rs2_ctrl)
        0: xRData1 = x0ff;
        1: xRData1 = x1ff;
        2: xRData1 = x2ff;
        3: xRData1 = x3ff;
        4: xRData1 = x4ff;
        5: xRData1 = x5ff;
        6: xRData1 = x6ff;
        7: xRData1 = x7ff;
        8: xRData1 = x8ff;
        9: xRData1 = x9ff;
        10: xRData1 = x10ff;
        11: xRData1 = x11ff;
        12: xRData1 = x12ff;
        13: xRData1 = x13ff;
        14: xRData1 = x14ff;
        15: xRData1 = x15ff;
        16: xRData1 = x16ff;
        17: xRData1 = x17ff;
        18: xRData1 = x18ff;
        19: xRData1 = x19ff;
        20: xRData1 = x20ff;
        21: xRData1 = x21ff;
        22: xRData1 = x22ff;
        23: xRData1 = x23ff;
        24: xRData1 = x24ff;
        25: xRData1 = x25ff;
        26: xRData1 = x26ff;
        27: xRData1 = x27ff;
        28: xRData1 = x28ff;
        29: xRData1 = x29ff;
        30: xRData1 = x30ff;
        31: xRData1 = x31ff;
        default: xRData1 = 0;
      endcase
   end

   // x0ff must be fixed to zero
   always @(posedge clk) begin 
      if (!rstn) begin
         x0ff <= 0;
      end
   end

   always @(posedge clk) begin
      if (!rstn) begin
         x1ff <= 0;
      end
      else begin
         if (xAddr == 1) begin
            if (xWEn) begin
               x1ff <= xWData;
            end
         end
      end
   end

   always @(posedge clk) begin
      if (!rstn) begin
         x2ff <= 0;
      end
      else begin
         if (xAddr == 2) begin
            if (xWEn) begin
               x2ff <= xWData;
            end
         end
      end
   end

   always @(posedge clk) begin
      if (!rstn) begin
         x3ff <= 0;
      end
      else begin
         if (xAddr == 3) begin
            if (xWEn) begin
               x3ff <= xWData;
            end
         end
      end
   end

   always @(posedge clk) begin
      if (!rstn) begin
         x4ff <= 0;
      end
      else begin
         if (xAddr == 4) begin
            if (xWEn) begin
               x4ff <= xWData;
            end
         end
      end
   end

   always @(posedge clk) begin
      if (!rstn) begin
         x5ff <= 0;
      end
      else begin
         if (xAddr == 5) begin
            if (xWEn) begin
               x5ff <= xWData;
            end
         end
      end
   end

   always @(posedge clk) begin
      if (!rstn) begin
         x6ff <= 0;
      end
      else begin
         if (xAddr == 6) begin
            if (xWEn) begin
               x6ff <= xWData;
            end
         end
      end
   end

   always @(posedge clk) begin
      if (!rstn) begin
         x7ff <= 0;
      end
      else begin
         if (xAddr == 7) begin
            if (xWEn) begin
               x7ff <= xWData;
            end
         end
      end
   end

   always @(posedge clk) begin
      if (!rstn) begin
         x8ff <= 0;
      end
      else begin
         if (xAddr == 8) begin
            if (xWEn) begin
               x8ff <= xWData;
            end
         end
      end
   end

   always @(posedge clk) begin
      if (!rstn) begin
         x9ff <= 0;
      end
      else begin
         if (xAddr == 9) begin
            if (xWEn) begin
               x9ff <= xWData;
            end
         end
      end
   end

   always @(posedge clk) begin
      if (!rstn) begin
         x10ff <= 0;
      end
      else begin
         if (xAddr == 10) begin
            if (xWEn) begin
               x10ff <= xWData;
            end
         end
      end
   end

   always @(posedge clk) begin
      if (!rstn) begin
         x11ff <= 0;
      end
      else begin
         if (xAddr == 11) begin
            if (xWEn) begin
               x11ff <= xWData;
            end
         end
      end
   end

   always @(posedge clk) begin
      if (!rstn) begin
         x12ff <= 0;
      end
      else begin
         if (xAddr == 12) begin
            if (xWEn) begin
               x12ff <= xWData;
            end
         end
      end
   end

   always @(posedge clk) begin
      if (!rstn) begin
         x13ff <= 0;
      end
      else begin
         if (xAddr == 13) begin
            if (xWEn) begin
               x13ff <= xWData;
            end
         end
      end
   end

   always @(posedge clk) begin
      if (!rstn) begin
         x14ff <= 0;
      end
      else begin
         if (xAddr == 14) begin
            if (xWEn) begin
               x14ff <= xWData;
            end
         end
      end
   end

   always @(posedge clk) begin
      if (!rstn) begin
         x15ff <= 0;
      end
      else begin
         if (xAddr == 15) begin
            if (xWEn) begin
               x15ff <= xWData;
            end
         end
      end
   end

   always @(posedge clk) begin
      if (!rstn) begin
         x16ff <= 0;
      end
      else begin
         if (xAddr == 16) begin
            if (xWEn) begin
               x16ff <= xWData;
            end
         end
      end
   end

   always @(posedge clk) begin
      if (!rstn) begin
         x17ff <= 0;
      end
      else begin
         if (xAddr == 17) begin
            if (xWEn) begin
               x17ff <= xWData;
            end
         end
      end
   end

   always @(posedge clk) begin
      if (!rstn) begin
         x18ff <= 0;
      end
      else begin
         if (xAddr == 18) begin
            if (xWEn) begin
               x18ff <= xWData;
            end
         end
      end
   end

   always @(posedge clk) begin
      if (!rstn) begin
         x19ff <= 0;
      end
      else begin
         if (xAddr == 19) begin
            if (xWEn) begin
               x19ff <= xWData;
            end
         end
      end
   end

   always @(posedge clk) begin
      if (!rstn) begin
         x20ff <= 0;
      end
      else begin
         if (xAddr == 20) begin
            if (xWEn) begin
               x20ff <= xWData;
            end
         end
      end
   end

   always @(posedge clk) begin
      if (!rstn) begin
         x21ff <= 0;
      end
      else begin
         if (xAddr == 21) begin
            if (xWEn) begin
               x21ff <= xWData;
            end
         end
      end
   end

   always @(posedge clk) begin
      if (!rstn) begin
         x22ff <= 0;
      end
      else begin
         if (xAddr == 22) begin
            if (xWEn) begin
               x22ff <= xWData;
            end
         end
      end
   end

   always @(posedge clk) begin
      if (!rstn) begin
         x23ff <= 0;
      end
      else begin
         if (xAddr == 23) begin
            if (xWEn) begin
               x23ff <= xWData;
            end
         end
      end
   end

   always @(posedge clk) begin
      if (!rstn) begin
         x24ff <= 0;
      end
      else begin
         if (xAddr == 24) begin
            if (xWEn) begin
               x24ff <= xWData;
            end
         end
      end
   end

   always @(posedge clk) begin
      if (!rstn) begin
         x25ff <= 0;
      end
      else begin
         if (xAddr == 25) begin
            if (xWEn) begin
               x25ff <= xWData;
            end
         end
      end
   end

   always @(posedge clk) begin
      if (!rstn) begin
         x26ff <= 0;
      end
      else begin
         if (xAddr == 26) begin
            if (xWEn) begin
               x26ff <= xWData;
            end
         end
      end
   end

   always @(posedge clk) begin
      if (!rstn) begin
         x27ff <= 0;
      end
      else begin
         if (xAddr == 27) begin
            if (xWEn) begin
               x27ff <= xWData;
            end
         end
      end
   end

   always @(posedge clk) begin
      if (!rstn) begin
         x28ff <= 0;
      end
      else begin
         if (xAddr == 28) begin
            if (xWEn) begin
               x28ff <= xWData;
            end
         end
      end
   end

   always @(posedge clk) begin
      if (!rstn) begin
         x29ff <= 0;
      end
      else begin
         if (xAddr == 29) begin
            if (xWEn) begin
               x29ff <= xWData;
            end
         end
      end
   end

   always @(posedge clk) begin
      if (!rstn) begin
         x30ff <= 0;
      end
      else begin
         if (xAddr == 30) begin
            if (xWEn) begin
               x30ff <= xWData;
            end
         end
      end
   end

   always @(posedge clk) begin
      if (!rstn) begin
         x31ff <= 0;
      end
      else begin
         if (xAddr == 31) begin
            if (xWEn) begin
               x31ff <= xWData;
            end
         end
      end
   end
endmodule
