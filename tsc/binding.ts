import { AzkoyenOptions, IAzkoyen } from "./azkoyen.interface";
import { join } from 'path';

/* eslint-disable @typescript-eslint/no-var-requires */
const addons = require('node-gyp-build')(join(__dirname, '..'));

export var Azkoyen: {
  new (options: AzkoyenOptions): IAzkoyen
} = addons.Azkoyen;
