# Unencrypted Communication

Unencrypted data is unprotected information that is easily readable. Unencrypted data is a high security risk because it can be intercepted during transmission. Secure Sockets Layer (SSL) and its more modern and secure replacement, Transport Layer Security (TLS) is the protocol for encrypting HTTP traffic.

> [!Note]
> Modern SSL/TLS certificates use the TLS protocol, but SSL remains a popular acronym amongst security experts.

## How to penetrate test for this vulnerability

- Manually navigate to [https://{domainname}.com](https://127.0.0.1:5000) and inspect the certificate if any.
- Manually navigate to [http://{domainname}.com](http://127.0.0.1:5000) your should be redirected to [https://{domainname}.com](https://127.0.0.1:5000).
- Inspect network traffic using [Wireshark](https://www.wireshark.org/) or similar.

## How to countermeasure this vulnerability

- Implement HTTPS with a signed certificate from a Certificate Authority (CA).
- Configure DNS to enforce HTTPS.

## Important links

- [Let’s Encrypt](https://letsencrypt.org/docs/) is a free, automated, and open certificate authority (CA).
- Follow this tutorial to implement a [Flask Self-Signed TLS Certificate](https://yuxingonwork.medium.com/understand-https-with-a-python-flask-example-self-signed-certificate-ec2cd2e41567).
- [Cloudflare](https://www.cloudflare.com/en-gb/) offers cheap domain names, easy TLS/SSL certification security tools to enforce HTTPS transfer.
