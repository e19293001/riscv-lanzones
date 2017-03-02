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
                output [3:0]  RWStrobe,
                input         LEn
                );

   reg                 RRdy;
   reg [31:0]          RAddr;
   reg                 RWEn;
   reg [31:0]          RWData;
   reg [3:0]           RWStrobe;

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
   reg			DI_AUIPC_ctrl;
   reg         DI_ADD_ctrl;
   reg         DI_XOR_ctrl;
   reg         DI_OR_ctrl;
   reg         DI_SLT_ctrl;
   reg         DI_SLTU_ctrl;
   reg         DI_AND_ctrl;
   reg         DI_SRL_ctrl;
   reg         DI_SRA_ctrl;
   reg         DI_SUB_ctrl;
   reg         DI_SLL_ctrl;
   reg         DI_SW_ctrl;
   reg         DI_SB_ctrl;
   reg         DI_SH_ctrl;

   reg         DI_ORI_ctrl;
   reg         DI_SLTI_ctrl;
   reg         DI_SLTIU_ctrl;
   reg         DI_ANDI_ctrl;
   reg         DI_ADDI_ctrl;
   reg         DI_SLLI_ctrl;
   reg         DI_SRLI_ctrl;
   reg         DI_SRAI_ctrl;
   reg         DI_XORI_ctrl;

   reg         DI_LW_ctrl;
   reg         DI_LB_ctrl;
   reg         DI_LBU_ctrl;
   reg         DI_LW_ff;
   wire        DI_LW_w;
   wire        DI_LW_xctrl;
   wire        DI_LB_xctrl;
   wire        DI_LBU_xctrl;
   reg         DI_LB_ff;
   reg         DI_LBU_ff;
   reg         DI_LH_ctrl;
   wire        DI_LH_xctrl;
   reg         DI_LH_ff;
   reg         DI_LHU_ctrl;
   wire        DI_LHU_xctrl;
   reg         DI_LHU_ff;

   reg [6:0]   funct7_ctrl;
   reg [4:0]   rs1_ctrl;
   reg [4:0]   rs2_ctrl;
   reg [2:0]   funct3_ctrl;

   reg [31:0]  alu_outctrl;

   reg                 stallctrl;
   reg                 stallff;
   wire                fetchctrl;

   reg                 invalid_inst;

   assign FIctrl = (RRdy & RVld) ? 1 : 0;
   //assign DIctrl = 1;
   assign EXctrl = 1;
   assign MActrl = 1;
   assign WBctrl = 1;

   assign fetchctrl = stallff ? 0 : 1;

   assign DI_LW_w = (DI_LW_ctrl | DI_LW_ff) ? 1 : 0; // ?? 
   assign DI_LW_xctrl = (DI_LW_ff & RVld) ? 1 : 0;
   assign DI_LB_xctrl = (DI_LB_ff & RVld) ? 1 : 0;
   assign DI_LBU_xctrl = (DI_LBU_ff & RVld) ? 1 : 0;
   assign DI_LH_xctrl = (DI_LH_ff & RVld) ? 1 : 0;
   assign DI_LHU_xctrl = (DI_LHU_ff & RVld) ? 1 : 0;
   
   always @(posedge clk) begin
      if (!rstn) begin
         rdff <= 0;
      end
      else begin
         if (DI_LW_ctrl || DI_LH_ctrl || DI_LHU_ctrl || DI_LB_ctrl || DI_LBU_ctrl) begin
            rdff = rd_ctrl;
         end
      end
   end

   always @(posedge clk) begin
      if (!rstn) begin
         DI_LB_ff <= 0;
      end
      else begin
         if (DI_LB_ctrl | DI_LB_ctrl) begin
            DI_LB_ff <= 1;
         end
         else if (DI_LB_ff && RVld) begin
            DI_LB_ff <= 0;
         end
      end
   end

   always @(posedge clk) begin
      if (!rstn) begin
         DI_LBU_ff <= 0;
      end
      else begin
         if (DI_LBU_ctrl) begin
            DI_LBU_ff <= 1;
         end
         else if (DI_LBU_ff && RVld) begin
            DI_LBU_ff <= 0;
         end
      end
   end

   always @(posedge clk) begin
      if (!rstn) begin
         DI_LH_ff <= 0;
      end
      else begin
         if (DI_LH_ctrl) begin
            DI_LH_ff <= 1;
         end
         else if (DI_LH_ff && RVld) begin
            DI_LH_ff <= 0;
         end
      end
   end
   
   always @(posedge clk) begin
      if (!rstn) begin
         DI_LHU_ff <= 0;
      end
      else begin
         if (DI_LHU_ctrl) begin
            DI_LHU_ff <= 1;
         end
         else if (DI_LHU_ff && RVld) begin
            DI_LHU_ff <= 0;
         end
      end
   end
   
   always @(posedge clk) begin
      if (!rstn) begin
         DI_LW_ff <= 0;
      end
      else begin
         if (DI_LW_ctrl) begin
            DI_LW_ff <= 1;
         end
         else if (DI_LW_ff && RVld) begin
            DI_LW_ff <= 0;
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
         else if (invalid_inst) begin
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
            if (stallctrl && (DI_SW_ctrl || DI_SB_ctrl || DI_SH_ctrl)) begin
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
            else if (DI_SB_ctrl) begin
               RWData <= xRData1 & 32'hFF;
            end
            else if (DI_SH_ctrl) begin
               RWData <= xRData1 & 32'hFFFF;
            end
            else if (RVld) begin
               RWData <= 0;
            end
         end
      end
   end

   always @(posedge clk) begin
      if (!rstn) begin
         RWStrobe <= 0;
      end
      else begin
         if (!Halt) begin
            if (stallctrl && DI_SW_ctrl) begin
               RWStrobe <= 4'hF;
            end
            else if (DI_SB_ctrl) begin
               RWStrobe <= 4'b0001;
            end
            else if (DI_SH_ctrl) begin
               RWStrobe <= 4'b0011;
            end
            else if (RVld) begin
               RWStrobe <= 0;
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
      DI_AUIPC_ctrl = 0;
      DI_ADD_ctrl = 0;
      DI_XOR_ctrl = 0;
      DI_OR_ctrl = 0;
      DI_SLT_ctrl = 0;
      DI_SLTU_ctrl = 0;
      DI_AND_ctrl = 0;
      DI_SRL_ctrl = 0;
      DI_SRA_ctrl = 0;
      DI_SUB_ctrl = 0;
      DI_SLL_ctrl = 0;
      DI_SW_ctrl = 0;
      DI_SB_ctrl = 0;
      DI_SH_ctrl = 0;
      DI_LW_ctrl = 0;
      DI_LB_ctrl = 0;
      DI_LBU_ctrl = 0;
      DI_LH_ctrl = 0;
      DI_LHU_ctrl = 0;

      DI_ORI_ctrl = 0;
      DI_SLTI_ctrl = 0;
      DI_SLTIU_ctrl = 0;
      DI_ANDI_ctrl = 0;
      DI_ADDI_ctrl = 0;
      DI_SLLI_ctrl = 0;
      DI_SRLI_ctrl = 0;
      DI_SRAI_ctrl = 0;
      DI_XORI_ctrl = 0;

      rd_ctrl = 0;
      imm_ctrl = 0;
      funct7_ctrl = 0;
      funct3_ctrl = 0;
      rs1_ctrl = 0;
      rs2_ctrl = 0;
      stallctrl = 0;
      invalid_inst = 0;
      
      if (DIctrlff) begin
         case (opcode_instw)
           7'b0010011: begin
              imm_ctrl = FIff[31:20];
              rs1_ctrl = FIff[19:15];
              funct3_ctrl = FIff[14:12];
              rd_ctrl = FIff[11:7];

              case (FIff[14:12])
                3'b000: DI_ADDI_ctrl = 1;
                3'b001: begin
                   DI_SLLI_ctrl = 1;
                   imm_ctrl = {7'b0,FIff[24:20]};
                   end
                3'b101: begin
                   if (FIff[31:25] == 7'b0000000) begin
                      DI_SRLI_ctrl = 1;
                      imm_ctrl = {7'b0,FIff[24:20]};
                   end
                   else if (FIff[31:25] == 7'b0100000) begin
                      DI_SRAI_ctrl = 1;
                      imm_ctrl = {7'b0,FIff[24:20]};
                   end
                   else begin
                      DI_SRLI_ctrl = 1; 
                      invalid_inst = 1;
                      imm_ctrl = {7'b0,FIff[24:20]};
                   end
                end
                3'b100: DI_XORI_ctrl = 1;
                3'b110: DI_ORI_ctrl = 1;
                3'b010: DI_SLTI_ctrl = 1;
                3'b011: DI_SLTIU_ctrl = 1;
                3'b111: DI_ANDI_ctrl = 1;
                default: invalid_inst = 1; 
              endcase
           end
           7'b0110111: begin // LUI
              DI_LUI_ctrl = 1;
              rd_ctrl = FIff[11:7];
              imm_ctrl = FIff[31:12];
           end
           7'b0010111: begin // AUIPC
              DI_AUIPC_ctrl = 1;
              rd_ctrl = FIff[11:7];
              imm_ctrl = FIff[31:12];
           end
           7'b0110011: begin // R-type
              case (FIff[31:25])
                7'b0000000: begin
                   case (FIff[14:12])
                     3'b000: DI_ADD_ctrl = 1;
                     3'b100: DI_XOR_ctrl = 1;
                     3'b110: DI_OR_ctrl = 1;
                     3'b010: DI_SLT_ctrl = 1;
                     3'b011: DI_SLTU_ctrl = 1;
                     3'b111: DI_AND_ctrl = 1;
                     3'b101: DI_SRL_ctrl = 1;
                     3'b001: DI_SLL_ctrl = 1;
                     default: invalid_inst = 1;
                   endcase
                end
                7'b0100000: begin
                   case (FIff[14:12])
                     3'b000: DI_SUB_ctrl = 1;
                     3'b101: DI_SRA_ctrl = 1;
                     default: invalid_inst = 1;
                   endcase
                end
                default: invalid_inst = 1;
              endcase
              funct7_ctrl = FIff[31:25];
              rs2_ctrl = FIff[24:20];
              rs1_ctrl = FIff[19:15];
              funct3_ctrl = FIff[14:12];
              rd_ctrl = FIff[11:7];
           end
           7'b0100011: begin // store
              case (FIff[14:12])
                3'b000: DI_SB_ctrl = 1;
                3'b001: DI_SH_ctrl = 1;
                3'b010: DI_SW_ctrl = 1;
                default: invalid_inst = 1;
              endcase
              imm_ctrl = {FIff[31:25],FIff[11:7]};
              rs2_ctrl = FIff[24:20];
              rs1_ctrl = FIff[19:15];
              funct3_ctrl = FIff[14:12];
              stallctrl = 1; // stop the fetch to write to memory
           end
           7'b0000011: begin // LW
              case (FIff[14:12])
                3'b000: DI_LB_ctrl = 1;
                3'b001: DI_LH_ctrl = 1;
                3'b010: DI_LW_ctrl = 1;
                3'b100: DI_LBU_ctrl = 1;
                3'b101: DI_LHU_ctrl = 1;
                default: invalid_inst = 1;
              endcase
              imm_ctrl = FIff[31:20];
              rs1_ctrl = FIff[19:15];
              funct3_ctrl = FIff[14:12];
              rd_ctrl = FIff[11:7];
              stallctrl = 1; // stop the fetch to read from memory
           end          
           default: invalid_inst = 1;
         endcase
      end
   end

   // ALU
   always @* begin
      alu_outctrl = 0;
      if (DI_ADD_ctrl) begin
         alu_outctrl = xRData0 + xRData1;
      end
      else if (DI_XOR_ctrl) begin
         alu_outctrl = xRData0 ^ xRData1;
      end
      else if (DI_OR_ctrl) begin
         alu_outctrl = xRData0 | xRData1;
      end
      else if (DI_SLT_ctrl) begin
         alu_outctrl = ($signed(xRData0) < $signed(xRData1)) ? 1 : 0;
      end
      else if (DI_SLTU_ctrl) begin
         alu_outctrl = (xRData0 < xRData1) ? 1 : 0;
      end
      else if (DI_AND_ctrl) begin
         alu_outctrl = xRData0 & xRData1;
      end
      else if (DI_SRL_ctrl) begin
         alu_outctrl = xRData0 >> xRData1;
      end
      else if (DI_SRA_ctrl) begin
         alu_outctrl = $signed(xRData0) >>> xRData1;
      end
      else if (DI_SUB_ctrl) begin
         alu_outctrl = xRData0 - xRData1;
      end
      else if (DI_SLL_ctrl) begin
         alu_outctrl = xRData0 << xRData1;
      end
      else if (DI_SB_ctrl | DI_SH_ctrl | DI_SW_ctrl | DI_LW_ctrl | DI_LB_ctrl | DI_LBU_ctrl | DI_LH_ctrl | DI_LHU_ctrl) begin
         alu_outctrl = xRData0 + imm_ctrl;
      end
//      else if (DI_LH_ctrl) begin
//         alu_outctrl = xRData0[16:0] + imm_ctrl;
//      end
      else if (DI_ORI_ctrl) begin
         alu_outctrl = xRData0 | imm_ctrl;
      end
      else if (DI_SLTI_ctrl) begin
         alu_outctrl = ($signed(xRData0) < $signed(imm_ctrl)) ? 1 : 0;
      end
      else if (DI_SLTIU_ctrl) begin
         alu_outctrl = (xRData0 < imm_ctrl) ? 1 : 0;
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
      else if (DI_XORI_ctrl) begin
         alu_outctrl = xRData0 ^ imm_ctrl;
      end
      else if (DI_AUIPC_ctrl) begin
         alu_outctrl = PCff + imm_ctrl;
      end
   end

   // x register controller
   always @(posedge clk) begin
      if (!rstn) begin
         xWEn <= 0;
      end
      else begin
         if (DI_LUI_ctrl ||
             DI_AUIPC_ctrl ||
             DI_ADD_ctrl || 
             DI_XOR_ctrl || 
             DI_OR_ctrl || 
             DI_SLT_ctrl || 
             DI_SLTU_ctrl || 
             DI_AND_ctrl || 
             DI_SRL_ctrl || 
             DI_SRA_ctrl || 
             DI_SUB_ctrl || 
             DI_SLL_ctrl ||
             DI_ORI_ctrl ||
             DI_SLTI_ctrl ||
             DI_SLTIU_ctrl ||
             DI_ANDI_ctrl ||
             DI_ADDI_ctrl ||
             DI_SLLI_ctrl ||
             DI_SRLI_ctrl ||
             DI_SRAI_ctrl ||
             DI_XORI_ctrl ||
             DI_LB_xctrl ||
             DI_LBU_xctrl ||
             DI_LH_xctrl ||
             DI_LHU_xctrl ||
             DI_LW_xctrl) begin
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
                  DI_XOR_ctrl ||
                  DI_OR_ctrl ||
                  DI_SLT_ctrl ||
                  DI_SLTU_ctrl ||
                  DI_AND_ctrl ||
                  DI_SRL_ctrl ||
                  DI_SRA_ctrl ||
                  DI_SUB_ctrl ||
                  DI_SLL_ctrl ||
                  DI_ANDI_ctrl ||
                  DI_ADDI_ctrl ||
                  DI_SLLI_ctrl ||
                  DI_SRLI_ctrl ||
                  DI_SRAI_ctrl ||
                  DI_XORI_ctrl ||
                  DI_SLTI_ctrl ||
                  DI_SLTIU_ctrl ||
                  DI_AUIPC_ctrl ||
                  DI_ORI_ctrl) begin
            xWData <= alu_outctrl;
         end
         else if (DI_LB_xctrl) begin
            xWData <= RData[7] ? (RData & 32'hFF) | 32'hFFFFFF00 : RData & 8'hFF;
         end
         else if (DI_LBU_xctrl) begin
            xWData <= RData & 8'hFF;
         end
         else if (DI_LH_xctrl) begin
            xWData <= RData[15] ? (RData & 32'hFFFF) | 32'hFFFF0000 : RData & 8'hFFFF;
         end
         else if (DI_LHU_xctrl) begin
            xWData <= $signed(RData) & 16'hFFFF;
         end
         else if (DI_LW_xctrl) begin
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
                  DI_AUIPC_ctrl ||
                  DI_XOR_ctrl || 
                  DI_OR_ctrl || 
                  DI_SLT_ctrl || 
                  DI_SLTU_ctrl || 
                  DI_AND_ctrl || 
                  DI_SRL_ctrl || 
                  DI_SRA_ctrl || 
                  DI_SUB_ctrl ||
                  DI_SLL_ctrl ||
                  DI_ANDI_ctrl ||
                  DI_ADDI_ctrl ||
                  DI_SLLI_ctrl ||
                  DI_SRLI_ctrl ||
                  DI_SRAI_ctrl ||
                  DI_XORI_ctrl ||
                  DI_SLTI_ctrl ||
                  DI_SLTIU_ctrl ||
                  DI_ORI_ctrl) begin
            xAddr <= rd_ctrl;
         end
         else if (DI_SW_ctrl | DI_SB_ctrl | DI_SH_ctrl) begin
            xAddr <= rs2_ctrl;
         end
         else if (DI_LW_xctrl || DI_LB_xctrl || DI_LBU_xctrl || DI_LH_xctrl || DI_LHU_xctrl) begin
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
