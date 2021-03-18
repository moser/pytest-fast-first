# pytest fast first

When applying TDD, a key to successful, fast development is quick feedback. This
plugin tries to shorten the time to feedback by ordering fast tests before slower
ones.

It measures the runtime of your tests and on subsequent sessions orders faster tests
before slower ones. 


## Installation

```bash
pip install pytest-fast-first
```


## Options

* `--ff-inverse`: Inverts the order (can be used to optimize the runtime of a test
  suite when run with xdist)
* `--ff-group-by-module`: By default tests are just ordered by their runtime. If 
  you have module-scoped fixtures, this can help with better fixture reuse.

## State file

The plugin creates the file `.pytest-runtimes` in which it stores the runtimes
in JSON format. If you want runtime-based ordering in CI builds, you can check
it in to your version control system (you will have to live with merge
conflicts though).


## License: [MIT](https://opensource.org/licenses/MIT)

Copyright 2021 Martin Vielsmaier

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
