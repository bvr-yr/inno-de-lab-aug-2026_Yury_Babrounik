use std::io::{self, BufWriter, Write};

const RAW_USER_RECORD: &[u8; 48]
    = b" 10827 ; aLeXanDer_vLaDimiRov ; mInSk ; ACTIVE \n";

fn main() -> io::Result<()> {
    let num: usize = std::env::args()
        .nth(1)
        .and_then(|s| s.parse().ok())
        .unwrap_or(10_000);

    let stdout = io::stdout();
    let mut writer = BufWriter::with_capacity(64 * 1024, stdout.lock());

    for _ in 0..num {
        writer.write_all(RAW_USER_RECORD)?;
    }

    writer.flush()?;
    Ok(())
}
