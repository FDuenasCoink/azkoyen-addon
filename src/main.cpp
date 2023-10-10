#include <napi.h>
#include "azkoyen/Azkoyen.hpp"

Napi::Object InitAll(Napi::Env env, Napi::Object exports) {
  Azkoyen::Init(env, exports);
  return exports;
}

NODE_API_MODULE(azkoyen_addon, InitAll);