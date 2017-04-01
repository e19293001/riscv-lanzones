# include  <vpi_user.h>

static int vpi_dynmem_write_compiletf(char*user_data)
{
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

static int vpi_dynmem_write_calltf(char*user_data)
{
  vpi_printf("Hello, World!\n");
  s_vpi_value value_s;
  vpiHandle systf_handle, arg_itr, arg_handle;
  PLI_INT32 key, value;
  PLI_INT32 result;

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
  value = value_s.value.integer;

  vpi_printf("key: %0X value: %0d\n", key, value);
  return 0;
}

void vpi_dynmem_write_register()
{
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
  0
};
