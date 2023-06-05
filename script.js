import http from 'k6/http';
import { sleep } from 'k6';

export default function() {
  http.get('http://15.207.107.150:8008/records');
  sleep(1);
}
