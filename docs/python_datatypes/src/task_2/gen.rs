use std::io::{self, BufWriter, Write};

const RAW_TRANSACTIONS: [&str; 6] = [
    "SUCCESS:100\n",
    "FAILED:50\n",
    "SUCCESS:-10\n",
    "SUCCESS:0\n",
    "SUCCESS:250\n",
    "ERROR:200\n",
];

fn main() -> io::Result<()> {
    let num: usize = std::env::args()
        .nth(1)
        .and_then(|s| s.parse().ok())
        .unwrap_or(10_000);

    let stdout = io::stdout();
    let mut writer = BufWriter::with_capacity(64 * 1024, stdout.lock());

    for i in 0..num {
        writer.write_all(RAW_TRANSACTIONS[i % 6].as_bytes())?;
    }

    writer.flush()?;
    Ok(())
}
