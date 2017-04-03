#include <vpi_user.h>
#include <bst.h>

node *memassoc = NULL;

static int vpi_dynmem_read_compiletf(char*user_data) {
  vpiHandle systf_handle;
  vpiHandle arg_itr;
  vpiHandle arg_handle;

  PLI_INT32 tfarg_type;
  int err_flag = 0;

  systf_handle = vpi_handle(vpiSysTfCall, NULL);
  arg_itr = vpi_iterate(vpiArgument, systf_handle);
  if (arg_itr == NULL) {
    vpi_printf("ERROR: $dynmem_read requires 1 argument.\n");
    err_flag = 1;
  }
  arg_handle = vpi_scan(arg_itr);
  tfarg_type = vpi_get(vpiType, arg_handle);
  if ((tfarg_type != vpiReg) &&
      (tfarg_type != vpiIntegerVar) &&
      (tfarg_type != vpiConstant)) {
    vpi_printf("ERROR: $dynmem_read arg1 must be a number, variable or net\n");
    err_flag = 1;
  }
//  arg_handle = vpi_scan(arg_itr);
//  if (arg_handle == NULL) {
//    vpi_printf("ERROR: $dynmem_read requires 2nd argument\n");
//    err_flag = 1;
//  }
//  tfarg_type = vpi_get(vpiType, arg_handle);
//  if ((tfarg_type != vpiReg) &&
//      (tfarg_type != vpiIntegerVar) &&
//      (tfarg_type != vpiConstant)) {
//    vpi_printf("ERROR: $dynmem_read must be a number, variable or net\n");
//    err_flag = 1;
//  }
  if (vpi_scan(arg_itr) != NULL) {
    vpi_printf("ERROR: $dynmem_read requires 2 arguments; has too many\n");
    vpi_free_object(arg_itr);
    err_flag = 1;
  }

  if (err_flag) {
    vpi_control(vpiFinish, 1);
  }
    
  return 0;
}

static int vpi_dynmem_read_calltf(char*user_data) {
  s_vpi_value value_s;
  vpiHandle systf_handle, arg_itr, arg_handle;
  unsigned int key;
  mem memdata;

  systf_handle = vpi_handle(vpiSysTfCall, NULL);
  arg_itr = vpi_iterate(vpiArgument, systf_handle);
  if (arg_itr == NULL) {
    vpi_printf("ERROR: $dynmem_read failed to obtain systf arg handles\n");
    return(0);
  }

  arg_handle = vpi_scan(arg_itr);
  value_s.format = vpiIntVal;
  vpi_get_value(arg_handle, &value_s);
  key = value_s.value.integer;

  memdata.address = key;
  memdata.data = bst_search(memassoc,memdata);

  vpi_printf("[ vpi_dynmem_read_calltf ] memdata.data: %08X\n", memdata.data);

  value_s.value.integer = (PLI_INT32) memdata.data;
  
  vpi_put_value(systf_handle, &value_s, NULL, vpiNoDelay);
  vpi_printf("[ vpi_dynmem_read_calltf ] address: %08X data: %08X\n", memdata.address, memdata.data);

  return 0;
}

PLI_INT32 vpi_end_of_simulation(s_cb_data *callback_data) {
  vpi_printf("[ vpi_end_of_simulation ]\n");
  bst_free(memassoc);
  return 0;
}

void vpi_dynmem_read_register() {
  s_vpi_systf_data tf_data;
  s_cb_data cb_data_s;
  vpiHandle callback_handle;

  tf_data.type      = vpiSysFunc;
  tf_data.tfname    = "$dynmem_read";
  tf_data.calltf    = vpi_dynmem_read_calltf;
  tf_data.compiletf = vpi_dynmem_read_compiletf;
  tf_data.sizetf    = 0;
  tf_data.user_data = 0;
  vpi_register_systf(&tf_data);

  cb_data_s.reason = cbEndOfSimulation;
  cb_data_s.cb_rtn = vpi_end_of_simulation;
  cb_data_s.obj = NULL;
  cb_data_s.time = NULL;
  cb_data_s.value = NULL;
  cb_data_s.user_data = NULL;
  callback_handle = vpi_register_cb(&cb_data_s);
  vpi_free_object(callback_handle);
}

static int vpi_dynmem_write_compiletf(char*user_data) {
  vpiHandle systf_handle;
  vpiHandle arg_itr;
  vpiHandle arg_handle;

  PLI_INT32 tfarg_type;
  int err_flag = 0;

  systf_handle = vpi_handle(vpiSysTfCall, NULL);
  arg_itr = vpi_iterate(vpiArgument, systf_handle);
  if (arg_itr == NULL) {
    vpi_printf("ERROR: $dynmem_write requires 2 arguments.\n");
    err_flag = 1;
  }
  arg_handle = vpi_scan(arg_itr);
  tfarg_type = vpi_get(vpiType, arg_handle);
  if ((tfarg_type != vpiReg) &&
      (tfarg_type != vpiIntegerVar) &&
      (tfarg_type != vpiConstant)) {
    vpi_printf("ERROR: $dynmem_write arg2 must be a number, variable or net\n");
    err_flag = 1;
  }
  arg_handle = vpi_scan(arg_itr);
  if (arg_handle == NULL) {
    vpi_printf("ERROR: $dynmem_write requires 2nd argument\n");
    err_flag = 1;
  }
  tfarg_type = vpi_get(vpiType, arg_handle);
  if ((tfarg_type != vpiReg) &&
      (tfarg_type != vpiIntegerVar) &&
      (tfarg_type != vpiConstant)) {
    vpi_printf("ERROR: $dynmem_write must be a number, variable or net\n");
    err_flag = 1;
  }
  if (vpi_scan(arg_itr) != NULL) {
    vpi_printf("ERROR: $dynmem_write requires 2 arguments; has too many\n");
    vpi_free_object(arg_itr);
    err_flag = 1;
  }

  if (err_flag) {
    vpi_control(vpiFinish, 1);
  }
    
  return 0;
}

static int vpi_dynmem_write_calltf(char*user_data) {
  s_vpi_value value_s;
  vpiHandle systf_handle, arg_itr, arg_handle;
  unsigned int key, value;
  mem memdata;

  systf_handle = vpi_handle(vpiSysTfCall, NULL);
  arg_itr = vpi_iterate(vpiArgument, systf_handle);
  if (arg_itr == NULL) {
    vpi_printf("ERROR: $dynmem_write failed to obtain systf arg handles\n");
    return(0);
  }

  arg_handle = vpi_scan(arg_itr);
  value_s.format = vpiIntVal;
  vpi_get_value(arg_handle, &value_s);
  key = value_s.value.integer;

  arg_handle = vpi_scan(arg_itr);
  vpi_free_object(arg_itr);
  vpi_get_value(arg_handle, &value_s);
  value = (unsigned int) value_s.value.integer;

  memdata.address = key;
  memdata.data = value;
  memassoc = bst_insert(memassoc,memdata);
  
  vpi_printf("writing key: %08X value: %08X\n", key, value);
  return 0;
}

void vpi_dynmem_write_register() {
  s_vpi_systf_data tf_data;

  tf_data.type      = vpiSysTask;
  tf_data.tfname    = "$dynmem_write";
  tf_data.calltf    = vpi_dynmem_write_calltf;
  tf_data.compiletf = vpi_dynmem_write_compiletf;
  tf_data.sizetf    = 0;
  tf_data.user_data = 0;
  vpi_register_systf(&tf_data);
}

void (*vlog_startup_routines[])() = {
  vpi_dynmem_write_register,
  vpi_dynmem_read_register,
  0
};
